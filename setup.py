# Written by Sergio La Rosa (sergio.larosa89@gmail.com)
# Part of "splitnjoin" package
# https://github.com/SergioLaRosa/splitnjoin

from setuptools import setup

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = ''

setup(
    name='splitnjoin',
    version='0.72',
    description='Simple module for splitting binary files into multiple chunks/parts and viceversa (from chunks/parts to original file)',
    long_description=long_description,
    url='https://github.com/SergioLaRosa/splitnjoin',
    author='Sergio La Rosa',
    author_email='sergio.larosa89@gmail.com',
    license='MIT',
    packages=['splitnjoin'],
    zip_safe=False)
