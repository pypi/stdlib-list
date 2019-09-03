Usage
=====

Getting The List of Libraries
-----------------------------

``stdlib_list.stdlib_list`` returns the list of libraries in stdlib for any given version (by default, current python version).

In particular:

::

    In [1]: from stdlib_list import stdlib_list

    In [2]: libs = stdlib_list("3.4")

    In [3]: libs[:6]
    Out[3]: ['__future__', '__main__', '_dummy_thread', '_thread', 'abc', 'aifc']


Checking if a Module is part of stdlib
--------------------------------------

``stdlib_list.in_stdlib`` provides an efficient way to check if a module name is part of stdlib.
It relies on ``@lru_cache`` to cache the stdlib list and query results for similar calls. Therefore it is much more efficient than ``module_name in stdlib_list()`` especially if you wish to perform multiple checks.

In particular:

::

    >>> from stdlib_list import in_stdlib
    >>> in_stdlib('zipimport')  # built in
    True
    >>> in_stdlib('math')       # C-API stdlib module, but linked as extension (on my machine)
    True
    >>> in_stdlib('numpy')      # C-API extension, not stdlib
    False
    >>> in_stdlib('sys')        # built-in (and special)
    True
    >>> in_stdlib('os')         # Python code in stdlib
    True
    >>> in_stdlib('requests')   # Python code, not stdlib
    False


.. automodule:: stdlib_list
    :members: stdlib_list, in_stdlib
