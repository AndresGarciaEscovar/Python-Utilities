# Python Utilities

Repository that contains several Python utilities that can be used as a
submodule. Files and content:

## Files and Description.

- context_managers.py:

## Contents

- `context_managers.py`:
  - `class TempFile`: Creates Temporary text files that are deleted when the
    context manager is exited.
  - `class WorkingDirectory`: Changes the working directory to the specified
    path and returns to the original working directory when the context manager
    is exited.
- `latex_maker.py`: Creates a LaTeX file with the specified name and
  contents. The file can be compiled and its contents saved.

---

# TODO

## Next

- Text is now returned -> write the save function.

## Backlog

- Program can now be saved, write the compile function.
- Remember to return the text, or not...make a quick function to do this.
- Write to run as a function,  or as a package.
- Remember to remove packages that are not needed.
