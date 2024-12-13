# Utilities

Contains various utilities to help with development. These utilities are not
specific to any project and the code can be reused as a submodule within other
git repositories.

## Contents

This is a brief overview of the utilities available in this repository:

- [context_manager](#context-managers): A context manager to help with
  different tasks that require an initial setup and a cleanup.
- [exceptions](#exceptions): Custom exceptions to help with error
  handling.
- [validation](#validation): Functions to help with data validation.

## Context Managers

- [file_temp.py](context_managers/file_temp.py): A context manager to create a
  temporary file that is automatically deleted when the context manager is
  exited. The file can also be kept, if needed.

- [working.py](context_managers/working.py): A context manager to change the
  working directory to a specified path and then change it back to the original
  working directory when the context manager is exited.

## Exceptions

## Validation
