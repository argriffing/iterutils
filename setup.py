from distutils.core import setup

myversion_tuple = (0, 1, 4)
myversion = '.'.join(str(x) for x in myversion_tuple)

classifiers = [
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules']

# This seems like a standard method.
long_description = open('README.rst').read()

setup(
        name = 'iterutils',
        version = myversion,
        author = 'Raymond Hettinger and friends',
        author_email = '',
        license = 'http://docs.python.org/license.html',
        description = 'Itertools recipes.',
        url = 'http://pypi.python.org/pypi/iterutils',
        py_modules = ['iterutils'],
        long_description = long_description,
        classifiers = classifiers)
