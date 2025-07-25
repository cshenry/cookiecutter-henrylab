"""Sphinx configuration."""
from datetime import datetime


project = "Henry Lab Cookiecutter"
author = "Christopher Henry"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.intersphinx", "myst_parser"]
intersphinx_mapping = {"mypy": ("https://mypy.readthedocs.io/en/stable/", None)}
language = "en"
html_theme = "furo"
html_logo = "_static/logo.png"
linkcheck_ignore = [
    "codeofconduct.html",
    "https://github.com/pre-commit/pre-commit-hooks#",
    "https://opensource.org/license/mit",
    "https://github.com/pycqa/pep8-naming#",
    "https://github.com/PyCQA/mccabe#",
    "https://github.com/bosd/cookiecutter-uv-hypermodern-python/releases/tag/",
    "https://cookiecutter-hypermodern-python.readthedocs.io",
    "https://badgen.net/badge/status/alpha/d8624d",
    "https://www.gnu.org/software/bash/",
    "https://docs.astral.sh/uv/reference/build_failures/#why-does-uv-build-a-package",
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]
