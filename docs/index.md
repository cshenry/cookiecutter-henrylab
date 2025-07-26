# Henry Lab Cookiecutter

```{toctree}
---
hidden: true
maxdepth: 1
---

Quickstart <quickstart>
guide
contributing
Code of Conduct <code_of_conduct>
license
Changelog <https://github.com/chenry/cookiecutter-henrylab/releases>
```

```{include} ../README.md
---
start-after: <!-- badges-begin -->
end-before: <!-- badges-end -->
---
```

[Cookiecutter][Cookiecutter] template for a Python package
based on the [Hypermodern Python][Hypermodern Python] article series.

## Usage

```console
$ cookiecutter gh:chenry/cookiecutter-henrylab
```

## Features

```{include} ../README.md
---
start-after: <!-- features-begin -->
end-before: <!-- features-end -->
---
```

## FAQ

### What is this project about?

The mission of this project is to
enable current best practices
through modern Python tooling.

### What makes this project different from other Python templates?

This is a general-purpose template for Python libraries and applications.

Our goals are:

- Focus on simplicity and minimalism
- Promote code quality through automation
- Provide reliable and repeatable processes

The project template is centered around the following tools:

- [uv][1] for packaging and dependency management
- [Nox][2] for automation of checks and other development tasks
- [GitHub Actions][3] for continuous integration and delivery

### Why is this Python template called "hypermodern"?

[Hypermodernism][Hypermodernism] is a school of chess that dates back to more than a century ago.
If this setup ever goes out of fashion,
I can pretend it was my secret plan from the start.
All images on the
[associated blog][hypermodern python] show
[past visions][retrofuturism] of the future.

[1]: https://docs.astral.sh/uv/
[2]: https://nox.thea.codes/
[3]: https://github.com/features/actions
[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodernism]: https://en.wikipedia.org/wiki/Hypermodernism_(chess)
[retrofuturism]: https://en.wikipedia.org/wiki/Retrofuturism
