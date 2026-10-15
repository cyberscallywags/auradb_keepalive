# 📖 Wiki Template

Ready-to-publish wiki pages for Cyber Scallywags projects. These Markdown files
map 1:1 onto a GitHub (or GitLab) project wiki.

## Pages

| File                  | Wiki page          | Purpose                                  |
| --------------------- | ------------------ | ---------------------------------------- |
| `Home.md`             | Home               | Landing page / index                     |
| `_Sidebar.md`         | _(navigation)_     | Sidebar shown on every page (GitHub)     |
| `_Footer.md`          | _(footer)_         | Footer shown on every page (GitHub)      |
| `Getting-Started.md`  | Getting Started    | Quick onboarding                         |
| `Installation.md`     | Installation       | Full install instructions                |
| `Configuration.md`    | Configuration      | Environment variables & settings         |
| `Usage.md`            | Usage              | How to run / common tasks                |
| `Architecture.md`     | Architecture       | How it works, components, data flow      |
| `FAQ.md`              | FAQ                | Frequently asked questions               |
| `Troubleshooting.md`  | Troubleshooting    | Common problems & fixes                  |
| `Roadmap.md`          | Roadmap            | Planned work                             |

## Publishing to a GitHub wiki

A GitHub wiki is its own git repo at `<repo>.wiki.git`. You must create the
first page via the web UI once (**Wiki → Create the first page**) to initialise
it, then:

```bash
git clone https://github.com/cyberscallywags/{{REPO}}.wiki.git
cd {{REPO}}.wiki

# Copy these pages in (from the template)
cp /path/to/project-template/wiki/*.md .

# Replace placeholders, then publish
git add -A
git commit -m "docs: seed wiki from Cyber Scallywags template"
git push
```

> **Page names:** GitHub derives the page title from the filename, turning
> hyphens into spaces (`Getting-Started.md` → "Getting Started"). Link between
> pages with `[[Page Name]]` or `[text](Page-Name)`.
>
> **Special pages:** `_Sidebar.md` and `_Footer.md` render on every page.

## Publishing to a GitLab wiki

GitLab wikis work the same way (`<repo>.wiki.git`). GitLab uses `_sidebar.md`
(lowercase) and does not use `_Footer.md`; rename/adjust as needed.

## Placeholders

Same tokens as the rest of the template — see `../TEMPLATE.md`:
`{{PROJECT_NAME}}`, `{{REPO}}`, `{{DEFAULT_BRANCH}}`, `{{LANG}}`, etc.
