# Python Bindings from Lib

This project show the basic setup to create python bindings for a given C++ library, which we do not
have to compile, just link against it as we already would have the `.a` and/or `.so` pre-built
libraries.

## Installation

Install `uv` python package manager by following [its installation
docs](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

> ℹ️ The example files can be taken from the repo
> [bazel_cpp](https://github.com/ManuNaEira/bazel_cpp/tree/pybind-bazel):
>  - `liblib1.so` can be built with the command `bazel build //src/example/lib1:lib1`.
>  - The header file can be taken from [lib1.hpp](https://github.com/ManuNaEira/bazel_cpp/blob/pybind-bazel/src/example/lib1/lib1.hpp).

1. Paste your C++ pre-built library `.so` file in the `lib/` folder, like the example
   [liblib1.so](./lib/liblib1.so).
2. Paste the C++ header files of the library in the `include/` folder, like the example
   [lib1.hpp](./include/lib1.hpp).
3. Run `uv sync`, to create the python virtual environment and install the python package on it.
4. Run the test with `uv run pytest` and verify how the the functionality, coded
   in C++, is being accessed from python code.

Alternatively, run `uv build` at the root of the repository. It will built the python distribution
package which can then be installed with `pip` in any other project. The contents of this wheel file
can be checked with the VSCode task `Unzip lib1py Wheel`, which should be like (using `python 3.11`
and `linux x86_64` as the platform):
```
📂 wheel_contents/
├── 📂 lib1py/
    ├── __init__.py
    ├── _core.cpython-311-x86_64-linux-gnu.so
    ├── _core.pyi
    ├── liblib1.so
    └── py.typed
├── 📂 lib1py-0.1.0.dist-info/
    ├── METADATA
    ├── RECORD
    └── WHEEL
```
