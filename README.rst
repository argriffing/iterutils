
About iterutils
===============

These functions have been copied from the recipes
in the Python documentation for itertools:
http://docs.python.org/library/itertools.html#recipes

The following license applies to the Python documentation:
http://docs.python.org/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python

The idea to collect all of the itertools recipes into
a module named iterutils.py is from this post
by Alex Martelli on stackoverflow:
http://stackoverflow.com/questions/1639772


Installation
============

Because iterutils has been packaged for pypi,
it can be installed using::

    $ pip install iterutils


Usage
=====

After iterutils has been installed,
its functions can be imported and used as follows::

    >>> import iterutils
    >>> list(iterutils.pairwise('abc'))
    [('a', 'b'), ('b', 'c')]
