Module inclusion policy
=======================

Python is a dynamic language with a complex module system, including
modules that are created only at runtime or appear on specific
supported platforms.

This page exists to document ``stdlib-list``'s approach to module detection
and subsequent inclusion. It is not intended to be permanent, and may change
over time as Python itself changes (or our approach to module detection
improves).

Current guiding rules
---------------------

* Missing top-level modules **are a bug**: if a new version of Python adds a new
  top-level module, our failure to detect it should be considered a bug.

  Concretely: if ``examplemodule`` is present in Python 3.999, then it should be
  included in the ``stdlib_list("3.999")`` listing.

* Missing sub-modules are **best-effort**: if ``examplemodule`` contains
  ``examplemodule.foo.bar.baz.deeply.nested``, we make a best-effort attempt
  to detect each inner module but make no guarantee about doing so.

  Our rationale for this is that "stdlib-ness" is inherited from the parent
  module, even when not explicitly listed. In other words: anything that matches
  ``examplemodule.*`` is in the standard library by definition so long
  as ``exmaplemodule`` is in the standard library.

* Platform-specific modules are **best-effort**: ``stdlib-list`` is currently collected
  from Linux builds of CPython. This means that Windows- and macOS-specific modules
  (i.e., modules that aren't installed except for on those hosts) are not necessarily
  included.

  This includes top-level modules.

* Missing non-CPython modules are **not supported**: ``stdlib-list`` is implicitly
  a list of CPython's standard library modules, which are expected to be mirrored
  in other implementations of Python.

* Psuedo-modules are **not supported**: Python sometimes makes use of
  "pesudo-modules", i.e. namespaces placed into ``sys.modules`` that don't
  pass :py:func:`inspect.ismodule`. We don't currently support these, since the
  semantics for doing so are unclear.
  See `stdlib-list#117 <https://github.com/pypi/stdlib-list/issues/117>`__
  for additional details.

If you have a scenario not covered by the rules above, please file an issue!
