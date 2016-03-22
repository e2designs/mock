#!/usr/bin/env python

""" Playing with Mock """

class widget(object):

    """ Widget used for understanding Mock and pytest"""
    
    _defaultValue = 1

    def __init__(self, value=_defaultValue):
	print "Initialized"
	print "Value = ", value
	self.value = value

    def setValue(self, value):
	self.value = value
	self.countup(self.value)

    def countup(self, value):
	while value < 11:
	    print value
	    value += 1
