# Course syllabus organization

This repository contains source files for https://lpnu-llm.github.io/roadmap/. The whole repository is a Markdown wiki in the Obsidian format.

The site is redeployed on every push to the `main` branch.

`Index.md` is the entry point. It contains courses and their topics in teaching order. Lecture pages are grouped into one folder per course, and each topic is an Obsidian link to a separate Markdown page in that course folder. A topic page should contain all the details of the topic. Some sections are required, as we use them to generate the index page.


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

Each course should contain 15 weeks in total. The generator reads topic order from `Index.md` and uses `weeks` to make a topic span several schedule rows.

## Build the syllabus site

This is normally done on GitHub Actions when `main` is pushed. If you need to build locally, run:

```sh
uv run build_syllabus.py
```

This creates a generated `site/` directory containing the syllabus at `index.html` and one HTML page for every linked Markdown topic.
