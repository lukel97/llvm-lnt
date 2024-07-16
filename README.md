LLVM "Nightly Test" Infrastructure
==================================

*LNT* is an infrastructure for performance testing. The software itself
consists of two main parts, a web application for accessing and visualizing
performance data, and command line utilities to allow users to generate and
submit test results to the server.

The package was originally written for use in testing LLVM compiler
technologies, but is designed to be usable for the performance testing of any
software.

Layout
======

This directory and its subdirectories contain the LLVM nightly test
infrastructure. This is technically version "4.0" of the LLVM nightly test
architecture.

The infrastructure has the following layout:

 $ROOT/lnt - Top-level Python 'lnt' module

 $ROOT/lnt/server/db - Database schema, utilities, and examples of the LNT plist format.

 $ROOT/docs - Sphinx documentation for LNT.

 $ROOT/tests - Tests for the infrastructure.

For more information, see the web documentation, or docs/.

Building
========

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install --editable .
$ lnt <runserver|runtest|...>
```

Testing
=======

Testing is done by running tox from the top-level directory. It runs the tests
for Python 3 and checks code style.
