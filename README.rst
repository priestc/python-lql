.. image:: https://travis-ci.org/priestc/python-lql.png?branch=master
   :target: https://travis-ci.org/priestc/python-lql
  
python-lql
==========

Library Query Language parser and utilities for python.

What is Library Query Language?
-------------------------------

LQL is a simple, declarative language for defining sets of files across nodes
in the Library Net.

If you wish to write an application on the Library Platform,
you are going to need to use this library to parse queries between the two formats.

Think of LQL as a striped down version of SQL. LQL queries resemble SQL ``WHERE`` clauses.

Usage
-----

    >>> From LQL import Query
    >>> query = Query(as_string("including text contains 'foobar';")
    >>> query.as_list
    [["including", [["text", "contains", "foobar"]]]

This library is for converting LQL queries into s-expression form and back again to
string format.

    >>> from LQL import Query
    >>> query = Query(as_list=[["including", [["text", "contains", "foobar"]]])
    >>> query.as_string
    "including text contains 'foobar'"
