# Yiqiang Ye Academic Homepage

This repository hosts the GitHub Pages personal homepage for **Yiqiang Ye**.

The project is maintained in the style of compact academic GitHub Pages sites: Jekyll builds the site from configuration, navigation data, Markdown content, layouts, includes, Sass, and static assets.

## Repository structure

- `_config.yml` — site title, description, author profile, email, and social links.
- `_data/navigation.yml` — top navigation links and homepage anchor targets.
- `_pages/about.md` — homepage content: about, news, education, research, publications, honors, skills, and contact.
- `_layouts/`, `_includes/`, `_sass/`, `assets/` — Jekyll theme scaffold and styling.
- `images/` — avatar and research figures.
- `files/` — downloadable files such as the CV PDF.
- `scripts/validate_site.py` — lightweight static validation before pushing.

## Common edits

### Update profile metadata

Edit `_config.yml`:

```yaml
author:
  name: "Yiqiang Ye (叶毅强)"
  avatar: "/images/yiqiang-avatar.svg"
  email: "yaniszz085@gmail.com"
  github: "YanisYe"
```

Add Google Scholar, ORCID, LinkedIn, DBLP, or personal website links there when available.

### Update homepage content

Edit `_pages/about.md`. Each navigation section is controlled by a manual anchor, e.g.:

```html
<span class='anchor' id='publications'></span>
# 📝 Selected Publications
```

If a new section is added, also update `_data/navigation.yml`.

### Add files and images

- Put PDFs and downloadable materials in `files/`.
- Put homepage images in `images/` or `images/research/`.
- Use `{{ '/path/to/file' | relative_url }}` in Markdown/HTML so links work both locally and on GitHub Pages.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000/`.

If Ruby dependencies are unavailable, run the static validator first:

```bash
python3 scripts/validate_site.py
```

## Deployment

For the username repository `YanisYe/yeyiqiang.github.io`, GitHub Pages publishes from the default branch automatically after pushing to GitHub.

## Notes

- The current avatar is an initials placeholder because no real headshot was found in the provided materials. Replace `images/yiqiang-avatar.svg` with a real academic photo when ready.
- Publication statuses are intentionally conservative and follow the provided CV/source files.
- Theme scaffold is derived from the academic/minimal-mistakes style used by the reference homepage, with personal content rewritten for this repository.
