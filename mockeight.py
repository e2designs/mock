#!/usr/bin/env python

from mock import Mock

# The mock object
class Foo(object):
    # Instance properties
    _fooValue = 123

    def callFoo(self):
	pass

    def doFoo(self, argValue):
	pass

def test_Foopass():
    #Create the Mock object
    mockFoo = Mock(spec =Foo)
    print mockFoo
    
    mockFoo.doFoo("narf")
    mockFoo.doFoo.assert_called_with("narf")

def test_Foofail():
    #Create the Mock object
    mockFoo = Mock(spec =Foo)
    print mockFoo

    mockFoo.doFoo("zort")
    mockFoo.doFoo.assert_called_with("narf")
