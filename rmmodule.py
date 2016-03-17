#!/usr/bin/python

import os
import os.path

class RemovalService(object):
    """ A Service for removing objects from teh filesystem."""

    def rm(filename):
	if os.path.isfile(filename):
	    os.remove(filename)
