#!/usr/bin/env python
import json
import shutil
from pathlib import Path


def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.
    """
    path = Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys=True, indent=2)
        io.write("\n")


def remove_conditional_files():
    """Remove files and directories based on cookiecutter choices."""
    
    # Remove notebooks directory if not requested
    if "{{ cookiecutter.use_notebooks }}" != "true":
        notebooks_dir = Path("notebooks")
        if notebooks_dir.exists():
            shutil.rmtree(notebooks_dir)
    
    # Remove Docker file if not requested
    if "{{ cookiecutter.use_docker }}" != "true":
        dockerfile = Path("Dockerfile")
        if dockerfile.exists():
            dockerfile.unlink()
    
    # Remove FastAPI file if not requested
    if "{{ cookiecutter.use_fastapi }}" != "true":
        api_file = Path("src/{{ cookiecutter.package_name }}/api.py")
        if api_file.exists():
            api_file.unlink()


if __name__ == "__main__":
    reindent_cookiecutter_json()
    remove_conditional_files()
