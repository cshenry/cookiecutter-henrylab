**Prompt: Customize cookiecutter-uv-hypermodern-python for Christopher Henry**

I want you to help me fork and customize the [bosd/cookiecutter-uv-hypermodern-python](https://github.com/bosd/cookiecutter-uv-hypermodern-python) template to create a reusable base template for scientific Python projects at Argonne National Lab. This template will be used by researchers to create Python packages and APIs that are reproducible, portable, and ready for deployment.

### **Goals for Custom Template**

* Build a fork of bosd/cookiecutter-uv-hypermodern-python
* Add support for Argonne Lab conventions and scientific workflows
* Include tools for API services (FastAPI optional)
* Prepare it for further extension into a Jupyter notebook workflow template

### **Customization Tasks**

1. Fork and clone the repo.
2. **Rename the project internally as **cookiecutter-henry-hypermodern-python**.**
3. In **cookiecutter.json**, set default values like:
   * **author: **"Christopher Henry"
   * **email: **"chenry@anl.gov"
   * **license: **"MIT"
   * use_mkdocs: **true**
4. Add optional components:
   * ✅ **fastapi** (optional REST API scaffold)
   * **✅ **docker/Dockerfile** support**
5. Add a **notebooks/** directory with:
   * A **README.md** explaining usage
   * A **vibe.md** template for exploratory prompts
6. Tweak **README.md** to reflect Argonne National Laboratory branding and usage.
7. **Make sure **pyproject.toml** includes **ruff**, **pytest**, **mypy**, etc.**
8. Verify GitHub Actions still run correctly.
9. Test cookiecutter locally with: cookiecutter path/to/your/new/template
