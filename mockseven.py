#!/usr/bin/env python

from mock import Mock

# The mock object
class Foo(object):
    # Instance properties
    _fooValue = 123

    def callFoo(self):
	print "Foo:callFoo_"

    def doFoo(self, argValue):
	print "Foo:doFoo:input = ", argValue

def test_Foo():
    # Creating the mock object with side effect
    fooObj = Foo()

    fooList = [665, 666, 667]
    mockFoo = Mock(return_value = fooObj, side_effect = fooList)
    i = 1
    while i < 4:
	fooTest = mockFoo()
	print fooTest
	i += 1


