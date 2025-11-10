#include <pybind11/pybind11.h>
#include "lib1.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
  m.def("print_hello", &CLib1::PrintHello);
}
