# nhls_py

![Rust workflow](https://github.com/TEALab-org/nhls_py/actions/workflows/ruff.yml/badge.svg?branch=main)

A python module for utilizing [`nhls`](https://github.com/TEALab-org/nhls).
`nhls_py` is not bindings to a rust library.
Instead it generates rust code 
and executes binaries that utilize `nhls`as a dependency.
`nhls_py` requires that the user has [`rustup`](https://rustup.rs) installed.

Every session, prior to utilizing the library, please call `nhls_py.session_init()`.
This will ensure that the correct rust toolchain is available,
and a suitable build directory is setup.
By default all build artifacts will live in `~/.cache/nhls`, but
an alternative directory can optially be passed to `session_init`.

## Notebooks

A notebooks directory is included in the repository at least for now.
This makes it easier to develop without globally installing `nhls_py`.

