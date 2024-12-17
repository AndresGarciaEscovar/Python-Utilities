# Utilities

Contains various utilities to help with development. These utilities are not
specific to any project and the code can be reused as a submodule within other
git repositories.

The tests for these utilities are in the hidden directory `.tests` in the root
of the repository. The tests are written using the `unittest` module in Python.
To run the tests, you need to install the package, i.e., install the conda
environment using the `environment.yml` file:
```commandline
conda env create --file environment.yml
```
Then activate the environment:
```commandline
conda activate env_utilities
```
knowing that this command install the package in interactive debugging mode. To
run the tests navigate to the root of the repository and the to the
`src/utitlities` directory:
```text
cd <root directory>/src/utilities
```
and run the following command:
```bash
python3 -m unittest discover .tests/
```
This will run all the tests in the `.tests` directory. Of course, you can run
individual tests by specifying the test file:
```bash
python3 -m unittest .tests/test_file_temp.py
```

## Requirements

This repository requires Python $3.11.8$ or later. The code has not been tested
with earlier versions of Python, but it still may work with these earlier
versions; try at your own risk.

## Contents

This is a brief overview of the utilities available in this repository:

- [.tests](#tests): Contains the tests for the utilities.
- [context_manager](#context-managers): Several context managers to help with
  different tasks that require an initial setup and a cleanup.
- [exceptions](#exceptions): Custom exceptions to help with error handling.
- [general](#general): General utilities that do not fit in any other category.
- [validation](#validation): Functions to help with data validation.

## .tests

This directory contains the tests for the below utilities. The directory
structure is the same as the utilities directory, with the files named such
that they correspond to the utilities they are testing, with the prefix
`test_`.

## Context Managers

```commandline
src/utilities/context_managers
```

- [cfiles.py](src/utilities/context_managers/cfiles.py): A context manager to 
  create a temporary file that is automatically deleted when the context
  manager is exited; the file can also be kept, if needed.

- [cworking.py](src/utilities/context_managers/cworking.py): A context manager
  to change the working directory to a specified path and then change it back
  to the original working directory when the context manager is exited.

## Exceptions
    
```commandline
src/utilities/exceptions
```

- [ecollections.py](src/utilities/exceptions/ecollections.py): Custom
  exceptions related to collections.
- [enumbers.py](src/utilities/exceptions/enumbers.py): Custom exceptions
  related to numbers.
- [etypes.py](src/utilities/exceptions/etypes.py): Custom exceptions related to
  types.

## General

```commandline
src/utilities/general
```

- [gstrings.py](src/utilities/general/gstrings.py): General utilities related
  to strings.
- [gtypes.py](src/utilities/general/gtypes.py): General utilities related to
  types; in particular, contains the definition of various custom types.

## Validation

```commandline
src/utilities/validation
```

- [vgeneral.py](src/utilities/validation/vgeneral.py): General validation
  utilities.
- [vnumbers.py](src/utilities/validation/vnumbers.py): Validation utilities
  related to numbers.
