from distutils.core import setup

myversion_tuple = (0, 1, 0)
myversion = '.'.join(str(x) for x in myversion_tuple)

classifiers = [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules']

# This seems like a standard method.
long_description = open('README.rst').read()

setup(
        name = 'iterutils',
        version = myversion,
        author = '...',
        author_email = '...',
        description = 'Itertools recipes.',
        long_description = long_description,
        classifiers = classifiers,
        packages = ['iterutils'])
