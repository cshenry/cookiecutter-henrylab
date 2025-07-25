# {{ cookiecutter.friendly_name }}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})][pypi status]
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})][license]

[![Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Ruff codestyle][ruff badge]][ruff project]

> **A scientific Python project developed at Argonne National Laboratory**
> 
> This project follows best practices for reproducible, portable, and maintainable scientific software development.

## Features

- **Modern Python Development**: Built with `uv` for fast dependency management and packaging
- **Code Quality**: Comprehensive linting with `ruff`, type checking with `mypy`, and testing with `pytest`
- **Scientific Workflows**: Ready for data analysis, computational research, and scientific computing
{% if cookiecutter.use_fastapi == "true" -%}
- **REST API**: FastAPI-based web service for exposing computational capabilities
{%- endif %}
{% if cookiecutter.use_docker == "true" -%}
- **Containerization**: Docker support for reproducible deployment and environment isolation
{%- endif %}
{% if cookiecutter.use_notebooks == "true" -%}
- **Jupyter Integration**: Structured notebook directory for exploratory analysis and documentation
{%- endif %}
- **Documentation**: Automated documentation with Sphinx and Read the Docs
- **CI/CD**: GitHub Actions for automated testing, linting, and deployment

## Requirements

- Python 3.9+
- `uv` package manager (recommended) or `pip`

## Installation

### Using uv (Recommended)

```console
$ uv add {{cookiecutter.project_name}}
```

### Using pip

You can install _{{cookiecutter.friendly_name}}_ via [pip] from [PyPI]:

```console
$ pip install {{cookiecutter.project_name}}
```

### Development Installation

For development, clone the repository and install with development dependencies:

```console
$ git clone https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}.git
$ cd {{cookiecutter.project_name}}
$ uv sync --all-groups
```

## Usage

### Command Line Interface

```console
$ {{cookiecutter.project_name}} --help
```

{% if cookiecutter.use_fastapi == "true" -%}
### API Service

Start the FastAPI development server:

```console
$ uvicorn {{cookiecutter.package_name}}.api:app --reload
```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/docs`.

{%- endif %}
{% if cookiecutter.use_notebooks == "true" -%}
### Jupyter Notebooks

Start Jupyter for exploratory analysis:

```console
$ jupyter notebook notebooks/
```

See `notebooks/README.md` for more information about the notebook structure and best practices.

{%- endif %}
{% if cookiecutter.use_docker == "true" -%}
### Docker

Build and run with Docker:

```console
$ docker build -t {{cookiecutter.project_name}} .
$ docker run {{cookiecutter.project_name}}
```

{%- endif %}
For detailed usage instructions, please see the [Command-line Reference].

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from Christopher Henry's [cookiecutter-henry-hypermodern-python] template, 
which is based on [@cjolowicz]'s [uv hypermodern python cookiecutter] template.

**Developed at Argonne National Laboratory**

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[pypi status]: https://pypi.org/project/{{cookiecutter.project_name}}/
[read the docs]: https://{{cookiecutter.project_name}}.readthedocs.io/
[tests]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit
[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/charliermarsh/ruff
[cookiecutter-henry-hypermodern-python]: https://github.com/chenry/cookiecutter-henry-hypermodern-python
[uv hypermodern python cookiecutter]: https://github.com/bosd/cookiecutter-uv-hypermodern-python
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/LICENSE
[contributor guide]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/CONTRIBUTING.md
[command-line reference]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
