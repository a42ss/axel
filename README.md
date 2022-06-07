
Axel Command line interface (aCLI)
==================================

Axel (aCLI) is an interactive and configurable command line interface (CLI). The main reason of using aCLI is to keep all the tools for your project in the same place easy to document and update.

[![Total alerts](https://img.shields.io/lgtm/alerts/g/a42ss/axel.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/a42ss/axel/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/a42ss/axel.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/a42ss/axel/context:python)

[![Build](https://github.com/a42ss/axel/actions/workflows/python-package.yml/badge.svg)](https://github.com/a42ss/axel/actions/workflows/python-package.yml)


## Installation

```
$ pip install -r requirements.txt

$ python setup.py install
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

## GitVersion
docker run --rm -v "$(pwd):/repo" localhost:5005/a42/workstation-gitversion-toolset:latest /repo | jq -r '.FullSemVer'

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run axel cli application

$ axel --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `AxelCli`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it axel --help
```

Poetry commands
---------------

This project's dependencies are managed with poetry: 

```
    # creation command
    poetry new --src axel
         
    # install project dependencies
    poetry install --remove-untracked
```
