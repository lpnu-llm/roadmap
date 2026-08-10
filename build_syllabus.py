#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "Markdown>=3.7,<4",
# ]
# ///

"""Build an HTML syllabus and topic pages from Obsidian Markdown."""

from __future__ import annotations

import argparse
import html
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import cast
from urllib.parse import quote

import markdown  # pyright: ignore[reportMissingModuleSource]

EXPECTED_WEEKS = 15
SECTION_RE = re.compile(r"(?m)^##\s+(.+?)\s*$")
COURSE_RE = re.compile(r"(?m)^#\s+(.+?)\s*$")
WIKILINK_RE = re.compile(r"(?m)^\s*\d+\.\s+\[\[([^]]+)]]\s*$")
WIKILINK_INLINE_RE = re.compile(r"!?\[\[([^]]+)]]")
ORDERED_ITEM_RE = re.compile(r"^\d+\.\s+(.+)$")
ASSIGNMENT_TITLE_RE = re.compile(r"^\*\*(.+?[.!?])\*\*(?:\s+|$)")
INLINE_RE = re.compile(r"\[([^]]+)]\(([^)]+)\)|`([^`]+)`")


class BuildError(Exception):
    """Raised when the syllabus source does not follow the documented format."""


@dataclass(frozen=True)
class Arguments:
    index: Path
    output: Path
    title: str


@dataclass(frozen=True)
class TopicLink:
    target: str
    label: str


@dataclass(frozen=True)
class Topic:
    link: TopicLink
    source_path: Path
    weeks: int
    sections: dict[str, str]


@dataclass(frozen=True)
class Course:
    title: str
    topics: list[Topic]
    placeholder: str | None = None


def split_by_headings(text: str, pattern: re.Pattern[str]) -> list[tuple[str, str]]:
    matches = list(pattern.finditer(text))
    return [
        (
            match.group(1).strip(),
            text[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(text)].strip(),
        )
        for index, match in enumerate(matches)
    ]


def parse_wikilink(value: str) -> TopicLink:
    target_and_anchor, separator, alias = value.partition("|")
    target = target_and_anchor.split("#", 1)[0].strip()
    if not target:
        raise BuildError(f"Invalid empty wikilink: [[{value}]]")
    label = alias.strip() if separator else Path(target).name
    return TopicLink(target=target, label=label)


def parse_topic(path: Path, link: TopicLink) -> Topic:
    if not path.is_file():
        raise BuildError(f"Topic page does not exist: {path}")

    text = path.read_text(encoding="utf-8")
    weeks = 1
    declares_weeks = False
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            raise BuildError(f"Unclosed YAML frontmatter: {path}")
        frontmatter = text[4:end]
        match = re.search(r"(?m)^weeks:\s*(\d+)\s*$", frontmatter)
        if match:
            declares_weeks = True
            weeks = int(match.group(1))
        text = text[end + 5 :]

    if declares_weeks and weeks < 2:
        raise BuildError(f"Only multi-week topics may declare weeks: {path}")

    sections = dict(split_by_headings(text, SECTION_RE))
    missing = [name for name in ("Subtopics", "Assignment") if not sections.get(name)]
    if missing:
        raise BuildError(f"{path} is missing required sections: {', '.join(missing)}")

    return Topic(link=link, source_path=path, weeks=weeks, sections=sections)


def parse_courses(index_path: Path) -> list[Course]:
    source_dir = index_path.parent
    courses: list[Course] = []

    for title, body in split_by_headings(index_path.read_text(encoding="utf-8"), COURSE_RE):
        link_values = cast(list[str], WIKILINK_RE.findall(body))
        links = [parse_wikilink(value) for value in link_values]
        if not links:
            courses.append(Course(title=title, topics=[], placeholder=body or "TODO"))
            continue

        topics = [
            parse_topic(source_dir / f"{link.target}.md", link)
            for link in links
        ]
        total_weeks = sum(topic.weeks for topic in topics)
        if total_weeks != EXPECTED_WEEKS:
            raise BuildError(
                f"{title} has {total_weeks} weeks; expected {EXPECTED_WEEKS}"
            )
        courses.append(Course(title=title, topics=topics))

    if not courses:
        raise BuildError(f"No courses found in {index_path}")
    return courses


def render_inline(text: str) -> str:
    parts: list[str] = []
    position = 0
    for match in INLINE_RE.finditer(text):
        parts.append(html.escape(text[position : match.start()]))
        link_text, url, code = match.groups()
        if code is not None:
            parts.append(f"<code>{html.escape(code)}</code>")
        else:
            parts.append(
                f'<a href="{html.escape(url, quote=True)}">{html.escape(link_text)}</a>'
            )
        position = match.end()
    parts.append(html.escape(text[position:]))
    return "".join(parts)


def render_markdown_block(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(render_inline(lines[index][2:].strip()))
                index += 1
            output.append(
                '<ul class="compact">' + "".join(f"<li>{item}</li>" for item in items) + "</ul>"
            )
            continue

        ordered_match = ORDERED_ITEM_RE.match(line)
        if ordered_match:
            items = []
            while index < len(lines):
                item_match = ORDERED_ITEM_RE.match(lines[index])
                if not item_match:
                    break
                item = item_match.group(1).strip()
                hard = item.startswith("* ")
                if hard:
                    item = item[2:].strip()
                rendered = render_inline(item)
                if hard:
                    rendered = f'<span class="tag">optional hard</span> {rendered}'
                items.append(rendered)
                index += 1
            output.append("<ol>" + "".join(f"<li>{item}</li>" for item in items) + "</ol>")
            continue

        output.append(f"<p>{render_inline(line)}</p>")
        index += 1

    return "\n".join(output)


def render_assignment_titles(text: str) -> str:
    items: list[str] = []
    for line in (line.strip() for line in text.splitlines() if line.strip()):
        item_match = ORDERED_ITEM_RE.match(line)
        if not item_match:
            raise BuildError(f"Invalid assignment list item: {line}")

        item = item_match.group(1).strip()
        hard = item.startswith("* ")
        if hard:
            item = item[2:].strip()

        title_match = ASSIGNMENT_TITLE_RE.match(item)
        if not title_match:
            raise BuildError(f"Assignment must start with a bold title: {line}")
        title = title_match.group(1)
        word_count = len(re.findall(r"[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*", title))
        if not 3 <= word_count <= 6:
            raise BuildError(f"Assignment title must contain 3–6 words: {title}")

        rendered = f"<strong>{render_inline(title)}</strong>"
        if hard:
            rendered = f'<span class="tag">optional hard</span> {rendered}'
        items.append(rendered)

    return "<ol>" + "".join(f"<li>{item}</li>" for item in items) + "</ol>"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "course"


def relative_url(source: Path, output_dir: Path) -> str:
    relative = Path(os.path.relpath(source, output_dir))
    return "/".join(quote(part) for part in relative.parts)


def topic_output_path(topic: Topic, output_dir: Path) -> Path:
    return (output_dir / topic.link.target).with_suffix(".html")


def render_topic_rows(topic: Topic, first_week: int, output_dir: Path) -> str:
    subtopics = render_markdown_block(topic.sections["Subtopics"])
    extra = topic.sections.get("Extra topics", "").strip()
    if extra:
        subtopics += '\n<p class="extra-label">Extra:</p>\n' + render_markdown_block(extra)

    assignment = render_assignment_titles(topic.sections["Assignment"])
    topic_url = relative_url(topic_output_path(topic, output_dir), output_dir)
    topic_label = html.escape(topic.link.label)
    rowspan = f' rowspan="{topic.weeks}"' if topic.weeks > 1 else ""
    rows: list[str] = []

    for offset in range(topic.weeks):
        cells = [f'<td class="num">{first_week + offset:02d}</td>']
        if offset == 0:
            cells.extend(
                [
                    f'<td class="topic"{rowspan}><a href="{topic_url}">{topic_label}</a></td>',
                    f'<td{rowspan}>{subtopics}</td>',
                    f'<td{rowspan}>{assignment}</td>',
                ]
            )
        row_class = "topic-start" if offset == 0 else "topic-continuation"
        rows.append(f'<tr class="{row_class}">' + "".join(cells) + "</tr>")

    return "\n".join(rows)


def render_course(course: Course, output_dir: Path) -> str:
    course_id = slugify(course.title)
    heading = f'<h2 class="course-title" id="{course_id}">{html.escape(course.title)}</h2>'
    if not course.topics:
        return heading + f'\n<p class="meta">{render_inline(course.placeholder or "TODO")}</p>'

    rows: list[str] = []
    week = 1
    for topic in course.topics:
        rows.append(render_topic_rows(topic, week, output_dir))
        week += topic.weeks

    return f"""{heading}
<table>
  <colgroup>
    <col class="week-column">
    <col class="topic-column">
    <col class="content-column">
    <col class="content-column">
  </colgroup>
  <thead>
    <tr>
      <th>Week</th>
      <th>Topic</th>
      <th>Subtopics</th>
      <th>Assignment</th>
    </tr>
  </thead>
  <tbody>
{chr(10).join(rows)}
  </tbody>
</table>"""


STYLE = """
:root {
  --bg: #ffffff;
  --fg: #000000;
  --dim: #555555;
  --line: #000000;
  --link: #0000e0;
  --visited: #551a8b;
  --tag-bg: #eeeeee;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000000;
    --fg: #ffffff;
    --dim: #999999;
    --line: #ffffff;
    --link: #82b1ff;
    --visited: #c5a3ff;
    --tag-bg: #222222;
  }
}

* { box-sizing: border-box; }
html { font-size: 15px; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace;
  line-height: 1.55;
}
a { color: var(--link); }
a:visited { color: var(--visited); }
header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
  padding: 0.8rem 1.2rem;
  border-bottom: 1px dashed var(--line);
}
header .site-title {
  font-weight: bold;
  color: var(--fg);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
header nav { display: flex; gap: 1.2rem; }
header nav a,
header nav a:visited { color: var(--dim); }
header nav a:hover { color: var(--fg); }
main {
  max-width: 72ch;
  margin: 0 auto;
  padding: 2rem 1.2rem 0;
}
main.index { max-width: 78rem; }
h1 {
  font-size: 1.35rem;
  line-height: 1.3;
  margin: 0.5rem 0 1.2rem;
}
h2.course-title {
  font-size: 1.35rem;
  line-height: 1.3;
  letter-spacing: 0.04em;
  margin: 2.8rem 0 0.8rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px dashed var(--line);
}
p.lead { max-width: 72ch; }
ul { padding-left: 1.4rem; }
li { margin: 0.25rem 0; }
table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
  font-size: 0.85rem;
  margin: 1.5rem 0;
}
col.week-column { width: 6%; }
col.topic-column { width: 20%; }
col.content-column { width: 37%; }
th {
  text-align: left;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.78rem;
  border-bottom: 1px solid var(--line);
  padding: 0.45rem 0.6rem;
}
td {
  vertical-align: top;
  padding: 0.55rem 0.6rem;
}
tbody tr.topic-start:not(:first-child) td { border-top: 1px dashed var(--dim); }
td.num { color: var(--dim); }
td.topic { font-weight: bold; }
td ul.compact,
td ol {
  margin: 0;
  padding-left: 1.3rem;
}
td ul.compact li,
td ol li { margin: 0.1rem 0; }
td p { margin: 0.2rem 0; }
.extra-label {
  color: var(--dim);
  font-weight: bold;
  margin-top: 0.65rem;
}
.meta {
  color: var(--dim);
  font-size: 0.85rem;
}
.tag {
  display: inline-block;
  background: var(--tag-bg);
  padding: 0 0.4em;
  font-size: 0.78em;
  white-space: nowrap;
}
footer {
  margin-top: 4rem;
  padding: 1rem 1.2rem 2rem;
  border-top: 1px dashed var(--line);
  color: var(--dim);
  font-size: 0.85rem;
}
footer p { margin: 0.2rem 0; }
""".strip()


def render_document(courses: list[Course], title: str, output_path: Path) -> str:
    course_html = "\n\n".join(render_course(course, output_path.parent) for course in courses)
    page_title = html.escape(title)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<style>
{STYLE}
</style>
</head>
<body>
<header>
  <a class="site-title" href="#top">{page_title}</a>
  <nav><a href="#curriculum">curriculum</a></nav>
</header>
<main class="index" id="top">
  <h1>{page_title}</h1>
  <p class="lead">Each course is organized as a 15-week sequence. Multi-week topics span several week rows.</p>
  <div id="curriculum">
{course_html}
  </div>
</main>
<footer>
  <p>{page_title} &middot; generated from <code>Index.md</code> and linked topic pages</p>
  <p>Build with <code>uv run build_syllabus.py</code>.</p>
</footer>
</body>
</html>
"""


def markdown_wikilink(value: str, source_path: Path, source_dir: Path) -> str:
    target_and_anchor, separator, alias = value.partition("|")
    target, anchor_separator, anchor = target_and_anchor.partition("#")
    target = target.strip()
    if not target:
        raise BuildError(f"Invalid empty wikilink: [[{value}]]")

    label = alias.strip() if separator else Path(target).name
    target_path = Path(target)
    html_target = target_path.with_suffix(".html")
    relative_destination = Path(
        os.path.relpath(source_dir / html_target, source_path.parent)
    )
    encoded_destination = "/".join(
        quote(part) for part in relative_destination.parts
    )
    if anchor_separator:
        encoded_destination += f"#{quote(anchor.strip())}"
    return f"[{label}]({encoded_destination})"


def render_markdown_links(text: str, source_path: Path, source_dir: Path) -> str:
    return WIKILINK_INLINE_RE.sub(
        lambda match: markdown_wikilink(match.group(1), source_path, source_dir), text
    )


def markdown_body(source_path: Path, source_dir: Path) -> str:
    text = source_path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end == -1:
            raise BuildError(f"Unclosed YAML frontmatter: {source_path}")
        text = text[end + 5 :]
    linked_text = render_markdown_links(text, source_path, source_dir)
    linked_text = re.sub(
        r"(?m)^(\d+\.)\s+\*\s+",
        r'\1 <span class="tag">optional hard</span> ',
        linked_text,
    )
    return markdown.markdown(linked_text, extensions=["extra", "sane_lists"])


def render_topic_document(
    topic: Topic,
    site_title: str,
    output_path: Path,
    index_path: Path,
    source_dir: Path,
) -> str:
    page_title = topic.link.label
    body = markdown_body(topic.source_path, source_dir)
    index_url = relative_url(index_path, output_path.parent)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)} · {html.escape(site_title)}</title>
<style>
{STYLE}
</style>
</head>
<body>
<header>
  <a class="site-title" href="{index_url}">{html.escape(site_title)}</a>
  <nav><a href="{index_url}">curriculum</a></nav>
</header>
<main>
  <h1>{html.escape(page_title)}</h1>
{body}
</main>
<footer>
  <p>{html.escape(site_title)} &middot; generated from <code>{html.escape(topic.source_path.name)}</code></p>
</footer>
</body>
</html>
"""


def write_topic_pages(
    courses: list[Course],
    source_dir: Path,
    output_dir: Path,
    index_output: Path,
    title: str,
) -> None:
    topics = {topic.source_path: topic for course in courses for topic in course.topics}
    for topic in topics.values():
        destination = topic_output_path(topic, output_dir)
        destination.parent.mkdir(parents=True, exist_ok=True)
        document = render_topic_document(
            topic, title, destination, index_output, source_dir
        )
        _ = destination.write_text(document, encoding="utf-8")


def build(index_path: Path, output_path: Path, title: str) -> None:
    if not index_path.is_file():
        raise BuildError(f"Index file does not exist: {index_path}")
    courses = parse_courses(index_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_topic_pages(
        courses, index_path.parent, output_path.parent, output_path, title
    )
    document = render_document(courses, title, output_path)
    _ = output_path.write_text(document, encoding="utf-8")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument(
        "--index",
        type=Path,
        default=script_dir / "Index.md",
        help="source index (default: Index.md next to this script)",
    )
    _ = parser.add_argument(
        "--output",
        type=Path,
        default=script_dir / "site" / "index.html",
        help="output syllabus; topic HTML pages are written alongside it (default: site/index.html)",
    )
    _ = parser.add_argument(
        "--title",
        default="LLM Specialization",
        help="page and site title",
    )
    namespace = parser.parse_args()
    args = Arguments(
        index=cast(Path, namespace.index),
        output=cast(Path, namespace.output),
        title=cast(str, namespace.title),
    )

    try:
        build(args.index.resolve(), args.output.resolve(), args.title)
    except BuildError as error:
        raise SystemExit(f"error: {error}") from error

    print(f"Built {args.output.resolve()}")


if __name__ == "__main__":
    main()
