# Python Bindings from Lib

This project show the basic setup to create python bindings for a given C++ library, which we do not
have to compile, just link against it as we already would have the `.a` and or `.so` pre-built
libraries.

Initial project status after initializing the project with `uv init`, more specifically the
following command:
```bash
uv init --lib --build-backend scikit --name lib1py
```

## Installation

Install `uv` python package manager by following [its installation docs](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

1. Run `uv build` at the root of the repository.
2. Built python package should be available in the `dist/` folder.
