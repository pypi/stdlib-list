import sys
import unittest

import stdlib_list

PY2 = sys.version_info[0] == 2


class CurrentVersionBase(unittest.TestCase):
    def setUp(self):
        self.list = stdlib_list.stdlib_list(sys.version[:3])


class TestCurrentVersion(CurrentVersionBase):
    def test_string(self):
        self.assertIn("string", self.list)

    def test_list_is_sorted(self):
        self.assertEqual(sorted(self.list), self.list)

    def test_builtin_modules(self):
        """Check all top level stdlib packages are recognised."""
        unknown_builtins = set()
        for module_name in sys.builtin_module_names:
            if module_name not in self.list:
                unknown_builtins.add(module_name)

        self.assertFalse(sorted(unknown_builtins))


class TestSysModules(CurrentVersionBase):

    # This relies on invocation in a clean python environment using unittest
    # not using pytest.

    ignore_list = ["stdlib_list", "functools32", "tests", "_virtualenv_distutils"]

    def setUp(self):
        super(TestSysModules, self).setUp()
        self.maxDiff = None

    def test_preloaded_packages(self):
        """Check all top level stdlib packages are recognised."""
        not_stdlib = set()
        for module_name in sys.modules:
            pkg, _, module = module_name.partition(".")

            # https://github.com/jackmaney/python-stdlib-list/issues/29
            if pkg.startswith("_sysconfigdata_"):
                continue

            if pkg in self.ignore_list:
                continue

            # Avoid duplicating errors covered by other tests
            if pkg in sys.builtin_module_names:
                continue

            if pkg not in self.list:
                not_stdlib.add(pkg)

        self.assertFalse(sorted(not_stdlib))

    def test_preloaded_modules(self):
        """Check all stdlib modules are recognised."""
        not_stdlib = set()
        for module_name in sys.modules:
            pkg, _, module = module_name.partition(".")

            # https://github.com/jackmaney/python-stdlib-list/issues/29
            if pkg.startswith("_sysconfigdata_"):
                continue

            if pkg in self.ignore_list:
                continue

            # Avoid duplicating errors covered by other tests
            if module_name in sys.builtin_module_names:
                continue

            if PY2:
                # Python 2.7 creates sub-modules for imports
                if pkg in self.list and module in self.list:
                    continue

                # Python 2.7 deprecation solution for old names
                if pkg == "email":
                    mod = sys.modules[module_name]
                    if mod.__class__.__name__ == "LazyImporter":
                        continue

            if module_name not in self.list:
                not_stdlib.add(module_name)

        self.assertFalse(sorted(not_stdlib))


if __name__ == "__main__":
    unittest.main()
