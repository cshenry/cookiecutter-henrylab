# cookiecutter-henrylab

<!-- badges-begin -->

[Status][status badge]
[Python Version][github page]
[CalVer][calver]
[License][license]
[Tests][github actions page]
[pre-commit enabled][pre-commit project]
[Ruff codestyle][ruff project]

<!-- badges-end -->

[Cookiecutter][cookiecutter] template for scientific Python projects at in the Henry Lab at **Argonne National Laboratory**.

Derived from: https://github.com/bosd/cookiecutter-uv-hypermodern-python

## Documentation

- **[Quickstart Guide](docs/quickstart.md)** - Get started quickly with installation and basic usage
- **[User Guide](docs/guide.md)** - Comprehensive guide to using this cookiecutter template

## Features

- **Scientific Computing Ready**: Optimized for data analysis, computational research, and scientific workflows
- **Optional FastAPI Support**: REST API scaffolding for web services and computational endpoints
- **Optional Docker Support**: Containerization for reproducible deployments
- **Optional Jupyter Integration**: Structured notebook directory with templates for exploratory analysis
- **Modern Python Tooling**: Built with `uv`, `ruff`, `mypy`, and `pytest`

## Usage

```console
cookiecutter gh:cshenry/cookiecutter-henrylab
```

## Linting prior to git commit

You need to run the linter prior to pushing your code to github. Do so with this command, which should be run in the project directory.

```console
pre-commit run --all-files
```

## Features

<!-- features-begin -->

- Packaging and dependency management with [uv][uv]
- Test automation with [Nox][nox]
- Linting with [pre-commit][pre-commit] and [ruff][ruff]
- Continuous integration with [GitHub Actions][github actions]
- Documentation with [Sphinx][sphinx], [MyST][myst], and [Read the Docs][read the docs] using the [furo][furo] theme
- Automated uploads to [PyPI][pypi] and [TestPyPI][testpypi]
- Automated release notes with [Release Drafter][release drafter]
- Automated dependency updates with [Dependabot][dependabot]
- Code formatting with [ruff][ruff] and [Prettier][prettier]
- Import sorting with [ruff][ruff]
- Testing with [pytest][pytest]
- Code coverage with [Coverage.py][coverage.py]
- Coverage reporting with [Codecov][codecov]
- Command-line interface with [Click][click]
- Static type-checking with [mypy][mypy]
- Runtime type-checking with [Typeguard][typeguard]
- Check documentation examples with [xdoctest][xdoctest]
- Generate API documentation with [autodoc][autodoc] and [napoleon][napoleon]
- Generate command-line reference with [sphinx-click][sphinx-click]
- Manage project labels with [GitHub Labeler][github labeler]

The template supports Python 3.9, 3.10, 3.11, 3.12 and 3.13.

<!-- features-end -->

[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[status badge]: https://badgen.net/badge/status/alpha/d8624d
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: https://calver.org/
[github actions badge]: https://github.com/chenry/cookiecutter-henry-hypermodern-python/workflows/Tests/badge.svg
[github actions page]: https://github.com/chenry/cookiecutter-henry-hypermodern-python/actions?workflow=Tests
[github page]: https://github.com/chenry/cookiecutter-henry-hypermodern-python
[license badge]: https://img.shields.io/github/license/chenry/cookiecutter-henry-hypermodern-python
[license]: https://opensource.org/license/mit
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/pypi/pyversions/cookiecutter-henry-hypermodern-python
[ruff project]: https://github.com/charliermarsh/ruff
[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
