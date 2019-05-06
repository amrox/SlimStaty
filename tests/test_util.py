#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from slimstaty import util


class TestCamelCasel(unittest.TestCase):

    def test_camel_case(self):
        assert util.camel_case("") == ""
        assert util.camel_case("a") == "a"
        assert util.camel_case("A") == "a"
        assert util.camel_case("fooBar") == "fooBar"
        assert util.camel_case("FooBar") == "fooBar"
        assert util.camel_case("foo_bar") == "fooBar"
        assert util.camel_case("foo-bar") == "fooBar"
        assert util.camel_case("Foo-Bar") == "fooBar"

    def test_camel_case_upper(self):
        assert util.camel_case("", uppercase_first_letter=True) == ""
        assert util.camel_case("a", uppercase_first_letter=True) == "A"
        assert util.camel_case("A", uppercase_first_letter=True) == "A"
        assert util.camel_case("fooBar", uppercase_first_letter=True) == "FooBar"
        assert util.camel_case("FooBar", uppercase_first_letter=True) == "FooBar"
        assert util.camel_case("foo_bar", uppercase_first_letter=True) == "FooBar"
        assert util.camel_case("foo-bar", uppercase_first_letter=True) == "FooBar"
        assert util.camel_case("Foo-Bar", uppercase_first_letter=True) == "FooBar"
