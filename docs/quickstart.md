# Quickstart Guide

## Requirements

Install [Cookiecutter][cookiecutter]:

```console
$ pipx install cookiecutter
```

Install [uv][uv] by downloading and running the install script:

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install [Nox][nox]:

```console
$ pipx install nox
```

[pipx][pipx] is preferred, but you can also install with `pip install --user`.

It is recommended to set up Python 3.9, 3.10, 3.11, 3.12 and 3.13 using [pyenv][pyenv].

## Creating a project

Generate a Python project:

```console
$ cookiecutter gh:cshenry/cookiecutter-henrylab
```

Change to the root directory of your new project,
and create a Git repository:

```console
$ git init
$ git add .
$ git commit
```

## Running

### Install uv Environment

```console
$ uv venv
$ uv sync
```

### Run the command-line interface from the source tree:

```console
$ uv run src/<project>
```

### Run an interactive Python session:

```console
$ uv run python
```

## Testing

Run the full test suite:

```console
$ nox
```

List the available Nox sessions:

```console
$ nox --list-sessions
```

Install the pre-commit hooks:

```console
$ nox -s pre-commit -- install
```

## Continuous Integration

### GitHub

1. Sign up at [GitHub][github].
2. Create an empty repository for your project.
3. Follow the instructions to push an existing repository from the command line.

### PyPI

1. Sign up at [PyPI][pypi].
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `PYPI_TOKEN` with the token you just copied.

### TestPyPI

1. Sign up at [TestPyPI][testpypi].
2. Go to the Account Settings on TestPyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `TEST_PYPI_TOKEN` with the token you just copied.

### Codecov

1. Sign up at [Codecov][codecov].
2. Install their GitHub app.

### Read the Docs

1. Sign up at [Read the Docs][read the docs].
2. Import your GitHub repository, using the button _Import a Project_.
3. Install the GitHub webhook,
   using the button _Add integration_
   on the _Integrations_ tab
   in the _Admin_ section of your project
   on Read the Docs.

## Releasing

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using [uv bump][uv bump].
3. Commit and push to GitHub.
4. Open a pull request.
5. Merge the pull request.

The Release workflow performs the following automated steps:

- Build and upload the package to PyPI.
- Apply a version tag to the repository.
- Publish a GitHub Release.

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

<!-- table-release-drafter-sections-begin -->

| Pull Request Label | Section in Release Notes     |
| ------------------ | ---------------------------- |
| `breaking`         | 💥 Breaking Changes          |
| `enhancement`      | 🚀 Features                  |
| `removal`          | 🔥 Removals and Deprecations |
| `bug`              | 🐞 Fixes                     |
| `performance`      | 🐎 Performance               |
| `testing`          | 🚨 Testing                   |
| `ci`               | 👷 Continuous Integration    |
| `documentation`    | 📚 Documentation             |
| `refactoring`      | 🔨 Refactoring               |
| `style`            | 💄 Style                     |
| `dependencies`     | 📦 Dependencies              |

<!-- table-release-drafter-sections-end -->

[codecov]: https://codecov.io/
[cookiecutter]: https://github.com/audreyr/cookiecutter
[github]: https://github.com/
[nox]: https://nox.thea.codes/
[pipx]: https://pipxproject.github.io/pipx/
[uv]: https://docs.astral.sh/uv/
[uv bump]: https://docs.astral.sh/uv/reference/cli/
[pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.org/
[read the docs]: https://readthedocs.org/
[testpypi]: https://test.pypi.org/
