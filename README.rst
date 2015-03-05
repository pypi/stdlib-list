Python Standard Library List
----------------------------

This package includes lists of all of the standard libraries for Python 2.6, 2.7, 3.2, 3.3, and 3.4, along with the code for scraping the official Python docs to get said lists.

Listing the modules in the standard library? Wait, why on Earth would you care about that?!
===========================================================================================

Because knowing whether or not a module is part of the standard library will come in handy in `a project of mine <https://github.com/jackmaney/pypt>`_. `And I'm not the only one <http://stackoverflow.com/questions/6463918/how-can-i-get-a-list-of-all-the-python-standard-library-modules>`_ who would find this useful. Or, the TL;DR answer is that it's handy in situations when you're analyzing Python code and would like to find module dependencies.

After googling for a way to generate a list of Python standard libraries (and looking through the answers to the previously-linked Stack Overflow question), I decided that I didn't like the existing solutions.

So, I decided to brute force it a bit, by putting together a scraper for the TOC of the standard library page of the official Python docs (eg `here is the page for Python 2.7 <https://docs.python.org/2/library/index.html>`_).

Usage
=====

The only argument you need to worry about specifying is a (major and minor) version number:

::
    
    >>> from stdlib_list import short_versions
    >>> short_versions
    ['2.6', '2.7', '3.2', '3.3', '3.4']

Or, if you prefer, an exact version of one of the standard library pages that I scraped:

::

    >>> from stdlib_list import long_versions
    >>> long_versions
    ['2.6.9', '2.7.9', '3.2.6', '3.3.6', '3.4.3']

With that in mind, here's how you can grab a list of standard libraries:

::

    >>> from stdlib_list import stdlib_list
    >>> libraries = stdlib_list("2.7")
    >>> libraries[:10]
    ['AL', 'BaseHTTPServer', 'Bastion', 'CGIHTTPServer', 'ColorPicker', 'ConfigParser', 'Cookie', 'DEVICE', 'DocXMLRPCServer', 'EasyDialogs']

Installation
============

The easy way is via ``pip``:

::

    pip install stdlib_list

The hard way is to clone this repository, go into the directory into which you cloned this repo, and do a

::

    python setup.py install


Caveats
=======

* No attempt was made to cull deprecated libraries. I just scraped the standard library page for the relevant version.

* For the sake of completion, if ``A.B`` is in the list, I also threw in ``A`` (eg, you'll find ``xml``, ``xml.etree``, and ``xml.etree.ElementTree`` in the list, even though ``xml`` isn't specifically listed in the TOC).

The Scraper
===========

You shouldn't need to fiddle around with the scraper, but in case you want to (or in case the Python Software Foundation decides to change the page layout of the standard library TOC page), just do:

::

    from stdlib_list import scraper
    scraper.scrape("2.7") # Scrape for 2.7 only (for debugging, mainly)
    scraper.scrape() # Scrape for all versions listed above.

LICENSE
=======

The MIT License (MIT)

Copyright (c) 2015 Jack Maney

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
