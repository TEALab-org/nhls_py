# nhls_py

A python module for utilizing [`NHLS`](https://github.com/TEALab-org/nhls).
`nhls_py` is not a set of bindings for a rust library.
Instead it generates rust code and executes binaries that utilize NHLS as a dependency.
`nhls_py` requires that the user has [`rustup`](https://rustup.rs) installed.
Every session, prior to utilizing the library, please call `nhls_py.session_init()`.
This will ensure that the correct rust toolchain is available, as well as the correct version of `NHLS`.

## Notebooks

A notebooks directory is included in the repository at least for now.
This makes it easier to develop without globally installing `nhls_py`.

