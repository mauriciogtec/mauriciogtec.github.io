# -- Project information -----------------------------------------------------

project = "Mauricio Tec"
copyright = "2024, Mauricio Tec"
author = "Mauricio Tec"

extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".nox/*",
    "README.md",
    "CLAUDE.md",
    "import_posts.ipynb",
    ".claude/**",
    "**/.ipynb_checkpoints/*",
]

# -- HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "",
    "show_nav_level": 0,
    "navbar_start": [],
    "navbar_center": [],
    "navbar_end": [],
    "navbar_persistent": [],
    "footer_start": [],
    "footer_center": [],
    "footer_end": [],
    "secondary_sidebar_items": [],
    "analytics": {"google_analytics_id": "G-D010PP32WC"},
}

html_favicon = "_static/profile-color-circle-small.png"
html_title = "Mauricio Tec"
html_static_path = ["_static"]
html_sidebars = {"**": []}

# -- OpenGraph --------------------------------------------------

ogp_site_url = "https://mauriciogtec.com"
ogp_social_cards = {
    "line_color": "#58a6ff",
}

# -- MyST and MyST-NB -------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

nb_execution_mode = "off"


def setup(app):
    app.add_css_file("custom.css")
