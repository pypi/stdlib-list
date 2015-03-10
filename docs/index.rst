.. Python Standard Library List documentation master file, created by
   sphinx-quickstart on Tue Mar 10 02:16:08 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Standard Library List
========================================================

This package includes lists of all of the standard libraries for Python 2.6, 2.7, 3.2, 3.3, and 3.4, along with the code for scraping the official Python docs to get said lists.

Listing the modules in the standard library? Wait, why on Earth would you care about that?!
===========================================================================================

Because knowing whether or not a module is part of the standard library will come in handy in `a project of mine <https://github.com/jackmaney/pypt>`_. `And I'm not the only one <http://stackoverflow.com/questions/6463918/how-can-i-get-a-list-of-all-the-python-standard-library-modules>`_ who would find this useful. Or, the TL;DR answer is that it's handy in situations when you're analyzing Python code and would like to find module dependencies.

After googling for a way to generate a list of Python standard libraries (and looking through the answers to the previously-linked Stack Overflow question), I decided that I didn't like the existing solutions.

So, I decided to brute force it a bit, by putting together a scraper for the TOC of the standard library page of the official Python docs (eg `here is the page for Python 2.7 <https://docs.python.org/2/library/index.html>`_).

Contents
========

.. toctree::
   :maxdepth: 2

   install
   usage
   metadata
   scraper



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
