cmake_minimum_required(VERSION 3.15)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

# Add include directory
include_directories(include)

# Find the compiled library, store its full path in the variable `LIB1_LIBRARY`
find_library(LIB1_LIBRARY 
    NAMES lib1
    PATHS lib
    NO_DEFAULT_PATH
    REQUIRED
)

# Create the pybind11 module
pybind11_add_module(_core MODULE src/main.cpp)

# Set RPATH to look in the same directory as the module
set_target_properties(_core PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH TRUE
)

# Link the library to the module
target_link_libraries(_core PRIVATE ${LIB1_LIBRARY})

# Add include directories to the target
target_include_directories(_core PRIVATE include)

# Installs the compiled Python extension module into the package directory named
# after `SKBUILD_PROJECT_NAME`.
install(TARGETS _core DESTINATION ${SKBUILD_PROJECT_NAME})
# Installs the external library file (lib1.so or lib1.a) into the same directory
# as the Python module. Ensures the module can find the library at runtime.
install(FILES ${LIB1_LIBRARY} DESTINATION ${SKBUILD_PROJECT_NAME})
