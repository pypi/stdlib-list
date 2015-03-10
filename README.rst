Python Standard Library List
----------------------------

This package includes lists of all of the standard libraries for Python 2.6, 2.7, 3.2, 3.3, and 3.4, along with the code for scraping the official Python docs to get said lists.

Listing the modules in the standard library? Wait, why on Earth would you care about that?!
===========================================================================================

Because knowing whether or not a module is part of the standard library will come in handy in `a project of mine <https://github.com/jackmaney/pypt>`_. `And I'm not the only one <http://stackoverflow.com/questions/6463918/how-can-i-get-a-list-of-all-the-python-standard-library-modules>`_ who would find this useful. Or, the TL;DR answer is that it's handy in situations when you're analyzing Python code and would like to find module dependencies.

After googling for a way to generate a list of Python standard libraries (and looking through the answers to the previously-linked Stack Overflow question), I decided that I didn't like the existing solutions. So, I used Beautiful Soup 4 to build a scraper and scraped the list of libraries (along with a bit of metadata) from the Python Module Index.

Usage
=====

::

    >>> from stdlib_list import stdlib_list
    >>> libraries = stdlib_list("2.7")
    >>> libraries[:10]
    ['AL', 'BaseHTTPServer', 'Bastion', 'CGIHTTPServer', 'ColorPicker', 'ConfigParser', 'Cookie', 'DEVICE', 'DocXMLRPCServer', 'EasyDialogs']

For more details, check out `the docs <http://python-stdlib-list.readthedocs.org/en/latest/>`_.
