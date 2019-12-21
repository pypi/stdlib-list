import difflib
import os
import os.path
import sys
import unittest
from distutils.sysconfig import get_python_lib
from sysconfig import get_config_var

import stdlib_list

try:
    sys.base_prefix
    has_base_prefix = sys.base_prefix != sys.prefix
except AttributeError:
    has_base_prefix = False

shlib_ext = get_config_var("SHLIB_SUFFIX") or get_config_var("SO")

tk_libs = get_config_var("TKPATH")


class UnifiedDiffAssertionError(AssertionError):
    def __init__(self, expected, got, msg="Differences"):
        super(UnifiedDiffAssertionError, self).__init__(self)
        filename = "stdlib_list/lists/{}.txt".format(sys.version[:3])
        diff = difflib.unified_diff(
            expected, got, lineterm="", fromfile="a/" + filename, tofile="b/" + filename
        )
        self.description = "{name}\n{diff}".format(name=msg, diff="\n".join(diff))

    def __str__(self):
        return self.description


class CurrentPlatformBase(object):

    dir = None
    ignore_test = False

    def setUp(self):
        self.list = stdlib_list.stdlib_list(sys.version[:3])
        if self.dir:
            self.assertTrue(os.path.isdir(self.dir))

    def _collect_shared(self, name):
        # stdlib extensions are not in subdirectories
        if "/" in name:
            return None

        return name.split(".", 1)[0]

    def _collect_file(self, name):
        if name.endswith(shlib_ext):
            return self._collect_shared(name)

        if not name.endswith(".py"):
            return None

        # This excludes `_sysconfigdata_m_linux_x86_64-linux-gnu`
        # https://github.com/jackmaney/python-stdlib-list/issues/29
        if "-" in name:
            return None

        # Ignore this oddball stdlib test.test_frozen helper
        if name == "__phello__.foo.py":
            return None

        if name.endswith("/__init__.py"):
            return name[:-12].replace("/", ".")

        # Strip .py and replace '/'
        return name[:-3].replace("/", ".")

    def _collect_all(self, base):
        base = base + "/" if not base.endswith("/") else base
        base_len = len(base)
        modules = []

        for root, dirs, files in os.walk(base):
            for filename in files:
                relative_base = root[base_len:]
                relative_path = os.path.join(relative_base, filename)
                module_name = self._collect_file(relative_path)
                if module_name:
                    modules.append(module_name)

            # In-place filtering of traversal, removing invalid module names
            # and cache directories
            for dir in dirs:
                if "-" in dir:
                    dirs.remove(dir)
            if "__pycache__" in dirs:
                dirs.remove("__pycache__")

            if self.ignore_test and "test" in dirs:
                dirs.remove("test")

            # openSUSE custom module added to stdlib directory
            if "_import_failed" in dirs:
                dirs.remove("_import_failed")

        return modules

    def assertNoDiff(self, base, new):
        if base == new:
            self.assertEqual(base, new)
        else:
            raise UnifiedDiffAssertionError(got=sorted(new), expected=sorted(base))

    def test_dir(self):
        needed = set(self.list)
        items = self._collect_all(self.dir)
        for item in items:
            if item not in self.list:
                needed.add(item)

        self.assertNoDiff(set(self.list), needed)


class TestPureLibDir(CurrentPlatformBase, unittest.TestCase):
    def setUp(self):
        self.dir = get_python_lib(standard_lib=True, plat_specific=False)
        super(TestPureLibDir, self).setUp()


class TestPlatLibDir(CurrentPlatformBase, unittest.TestCase):
    def setUp(self):
        self.dir = get_python_lib(standard_lib=True, plat_specific=True)
        super(TestPlatLibDir, self).setUp()


class TestSharedDir(CurrentPlatformBase, unittest.TestCase):
    def setUp(self):
        self.dir = get_config_var("DESTSHARED")
        super(TestSharedDir, self).setUp()


if has_base_prefix:

    class TestBasePureLibDir(CurrentPlatformBase, unittest.TestCase):
        def setUp(self):
            base = sys.base_prefix
            self.dir = get_python_lib(
                standard_lib=True, plat_specific=False, prefix=base
            )
            super(TestBasePureLibDir, self).setUp()

    class TestBasePlatLibDir(CurrentPlatformBase, unittest.TestCase):
        def setUp(self):
            base = sys.base_prefix
            self.dir = get_python_lib(
                standard_lib=True, plat_specific=True, prefix=base
            )
            super(TestBasePlatLibDir, self).setUp()


if tk_libs:
    tk_libs = tk_libs.strip(os.pathsep)

    class TestTkDir(CurrentPlatformBase, unittest.TestCase):

        # Python 2.7 tk-libs includes a `test` package, however it is
        # added to sys.path by test.test_tk as a top level directory
        # so test.widget_tests becomes module name `widget_tests`
        ignore_test = True

        def setUp(self):
            base = get_python_lib(standard_lib=True, plat_specific=False)
            self.dir = os.path.join(base, tk_libs)
            super(TestTkDir, self).setUp()


if __name__ == "__main__":
    unittest.main()
