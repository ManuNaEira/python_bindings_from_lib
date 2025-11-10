import sys
import unittest

import lib1py


class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(lib1py.print_hello(), "Hello")


if __name__ == "__main__":
    print(sys.version)
    unittest.main()
