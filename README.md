# cookiecutter-proj-template

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development and testing. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/fpgmaas/deptry/) and [prettier](https://prettier.io/)
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- Documentation with [MkDocs](https://www.mkdocs.org/)

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory. If you have cloned this repo, then run this command

```bash
pipx run cookiecutter <PATH_TO_THE_LOCAL_REPO>
```

You will be asked to provide some details about the project, like the name, github details, etc. An option to setup git upon creating the project is also available. Once these details are provided, a new project is setup.

Then CD into the project directory and nstall the environment and the pre-commit hooks with

```bash
cd <project-name>
make install
```

You are now ready to start development on your project!

## Acknowledgements

This project is partially based on [Florien Maas\'s](https://github.com/fpgmaas)\'s great
[cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry)
repository.