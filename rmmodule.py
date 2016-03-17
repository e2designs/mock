#!/usr/bin/python

import os
import os.path

class RemovalService(object):
    """ A Service for removing objects from the filesystem."""

    def rm(self, filename):
	print filename
	if os.path.isfile(filename):
	    os.remove(filename)
