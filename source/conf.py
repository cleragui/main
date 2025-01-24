# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Clera'
copyright = '2023, GNU LGPLv3'
author = 'Erasmus A. Junior'
# release = '0.2.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']
# html_theme = "sphinx_rtd_theme"
html_theme = 'sphinx_book_theme'
html_favicon = "_static/toon-icon.ico"
# html_logo = "_static/main-banner.png"

html_theme_options = {
    "logo": {
        "image_light": "_static/main-banner.png",
        "image_dark": "_static/main-banner-dark.png",
        "text": '<div id="sidebar_mini"><a href="https://pepy.tech/projects/clera" style="margin-right: 10px;"><img src="https://static.pepy.tech/badge/clera" alt="PyPI Downloads"></a><a href="https://pypi.org/project/clera/"><img src="https://img.shields.io/pypi/v/clera"></a></div>',
    },
}

html_css_files = ["custom.css"]