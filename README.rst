
About iterutils
===============

These functions have been taken from the recipes_
in the Python documentation for itertools.
They were originally written by
Raymond Hettinger and various other people.

This license_
applies to the Python documentation.

The idea to collect all of the itertools recipes into
a module named iterutils is from this post_
by Alex Martelli.


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


.. _recipes: http://docs.python.org/library/itertools.html#recipes
.. _license: http://docs.python.org/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python
.. _post: http://stackoverflow.com/questions/1639772
