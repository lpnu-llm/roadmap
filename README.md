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

1. ...
2. * Optional hard assignment

## Extra topics

- ...
```

Omit `Resources` and `Extra topics` when they are empty. Mark optional hard assignments with `*` after the list number.

A topic normally takes one week. If it takes more than one week, add YAML frontmatter:

```yaml
---
weeks: 2
---
```

Do not add `weeks` for a one-week topic. A multi-week page uses the same sections as a one-week page; do not split it into weekly subsections.

Each course should contain 15 weeks in total. A future generator can read topic order from `Index.md` and use `weeks` to make a topic span several schedule rows.
