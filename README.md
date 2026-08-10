# Course syllabus organization

`Index.md` is the entry point. It contains courses and their topics in teaching order. Each topic is an Obsidian link to a separate Markdown page.

Keep topic details out of `Index.md`. Put them on the topic page instead.

## Topic page format

Use these sections in this order:

```md
## Subtopics

- ...

## Reading

- ...

## Resources

- ...

## Assignment

1. **Short assignment title.** Full assignment details.
2. * **Optional hard assignment.** Full assignment details.

## Extra topics

- ...
```

Omit `Resources` and `Extra topics` when they are empty. Start every assignment with a bold title of 3–6 words, followed by the full details. Mark optional hard assignments with `*` after the list number. The generated HTML shows only assignment titles; the topic page keeps the complete instructions.

A topic normally takes one week. If it takes more than one week, add YAML frontmatter:

```yaml
---
weeks: 2
---
```

Do not add `weeks` for a one-week topic. A multi-week page uses the same sections as a one-week page; do not split it into weekly subsections.

Each course should contain 15 weeks in total. The generator reads topic order from `Index.md` and uses `weeks` to make a topic span several schedule rows.

## Build the syllabus site

Run:

```sh
uv run build_syllabus.py
```

This creates a generated `site/` directory containing the syllabus at `index.html` and one HTML page for every linked Markdown topic. Obsidian wiki links are converted to relative HTML links, so generated topic pages can reference each other. The source files are not changed.

Use `--output` to choose the syllabus file and, implicitly, the directory for generated topic pages; use `--title` to change the page title:

```sh
uv run build_syllabus.py --output public/index.html --title "LLM Courses"
```

## Deploy to GitHub Pages

The `Deploy GitHub Pages` workflow builds and deploys `site/` whenever `main` is pushed. It can also be run manually from the repository's **Actions** tab.

Before the first deployment, open **Settings → Pages** in GitHub and set **Build and deployment → Source** to **GitHub Actions**. No deploy branch, secret, or personal access token is required; the workflow uses GitHub's built-in Pages permissions.
