# cookiecutter-henrylab

<!-- badges-begin -->

[Status][status badge]
[Python Version][github page]
[CalVer][calver]
[License][license]
[Read the documentation][readthedocs page]
[Tests][github actions page]
[Codecov][codecov page]
[pre-commit enabled][pre-commit project]
[Ruff codestyle][ruff project]
[Contributor Covenant][code of conduct]

<!-- badges-end -->

[Cookiecutter][Cookiecutter] template for scientific Python projects at in the Henry Lab at **Argonne National Laboratory**.

Based on the [Hypermodern Python][Hypermodern Python] article series and customized for scientific computing workflows.

✨📚✨ [Read the full documentation][readthedocs page]

Derived from: https://github.com/bosd/cookiecutter-uv-hypermodern-python

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

## Features

<!-- features-begin -->

- Packaging and dependency management with [uv][uv]
- Test automation with [Nox][Nox]
- Linting with [pre-commit][pre-commit] and [ruff][ruff]
- Continuous integration with [GitHub Actions][GitHub Actions]
- Documentation with [Sphinx][Sphinx], [MyST][MyST], and [Read the Docs][Read the Docs] using the [furo][furo] theme
- Automated uploads to [PyPI][PyPI] and [TestPyPI][TestPyPI]
- Automated release notes with [Release Drafter][Release Drafter]
- Automated dependency updates with [Dependabot][Dependabot]
- Code formatting with [ruff][ruff] and [Prettier][Prettier]
- Import sorting with [ruff][ruff]
- Testing with [pytest][pytest]
- Code coverage with [Coverage.py][Coverage.py]
- Coverage reporting with [Codecov][Codecov]
- Command-line interface with [Click][Click]
- Static type-checking with [mypy][mypy]
- Runtime type-checking with [Typeguard][Typeguard]
- Check documentation examples with [xdoctest][xdoctest]
- Generate API documentation with [autodoc][autodoc] and [napoleon][napoleon]
- Generate command-line reference with [sphinx-click][sphinx-click]
- Manage project labels with [GitHub Labeler][GitHub Labeler]

The template supports Python 3.9, 3.10, 3.11, 3.12 and 3.13.

<!-- features-end -->

[ruff badge]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff project]: https://github.com/charliermarsh/ruff
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: https://calver.org/
[code of conduct]: https://github.com/chenry/cookiecutter-henry-hypermodern-python/blob/main/CODE_OF_CONDUCT.md
[codecov badge]: https://codecov.io/gh/chenry/cookiecutter-henry-hypermodern-python/branch/main/graph/badge.svg
[codecov page]: https://codecov.io/gh/chenry/cookiecutter-henry-hypermodern-python
[contributor covenant badge]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
[github actions badge]: https://github.com/chenry/cookiecutter-henry-hypermodern-python/workflows/Tests/badge.svg
[github actions page]: https://github.com/chenry/cookiecutter-henry-hypermodern-python/actions?workflow=Tests
[github page]: https://github.com/chenry/cookiecutter-henry-hypermodern-python
[license badge]: https://img.shields.io/github/license/chenry/cookiecutter-henry-hypermodern-python
[license]: https://opensource.org/license/mit
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[python version badge]: https://img.shields.io/pypi/pyversions/cookiecutter-henry-hypermodern-python
[readthedocs badge]: https://img.shields.io/readthedocs/cookiecutter-henry-hypermodern-python/latest.svg?label=Read%20the%20Docs
[readthedocs page]: https://cookiecutter-henry-hypermodern-python.readthedocs.io/
[status badge]: https://badgen.net/badge/status/alpha/d8624d
[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[click]: https://click.palletsprojects.com/
[codecov]: https://codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[mypy]: https://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[uv]: https://docs.astral.sh/uv/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[ruff]: https://github.com/astral-sh/ruff
[sphinx]: https://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
