python-lql
==========

Library Query Language parser and utilities for python.

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