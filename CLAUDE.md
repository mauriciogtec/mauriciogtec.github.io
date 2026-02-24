# Mauricio Tec's Personal Website

## Project
Sphinx-based personal website and blog at **https://mauriciogtec.com**. Deployed via GitHub Actions to GitHub Pages.

## Stack
- **Framework:** Sphinx + MyST-NB + ABlog + pydata-sphinx-theme
- **Markup:** MyST Markdown (with colon fences, definition lists, html_image)
- **Build:** `nox -s docs` (static) | `nox -s docs -- live` (live preview)
- **Config:** `conf.py` (Sphinx), `requirements.txt` (Python deps)

## Key Conventions
- Blog posts go in `blog/YYYY/slug.md` or `blog/YYYY/slug.ipynb`
- Page sidebars defined in `conf.py html_sidebars`
- Custom CSS in `_static/custom.css` — keep changes minimal and targeted
- Templates in `_templates/` are Jinja2 extending pydata_sphinx_theme
- The D3.js social graph in `_templates/hello.html` is fragile — edit carefully
- `nb_execution_mode = "off"` by default — notebooks render but don't execute
- Publications auto-generated from ORCID via `scripts/orcid-publications.py`

## Owner Context
**Mauricio Tec** — Applied research scientist at Harvard (CS Dept + Data Science Initiative). Focus: reinforcement learning, LLMs, diffusion generative models. Background: PhD UT Austin, MSc Cambridge, BSc ITAM. Industry: Meta AI (FAIR), Intel AI, CIBanco.
