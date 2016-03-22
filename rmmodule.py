#!/usr/bin/python

""" Just a file used for mock tests"""

import os
import os.path

class RemovalService(object):
    """ A Service for removing objects from the filesystem."""

    def rm(self, filename):
	print filename
	if os.path.isfile(filename):
	    os.remove(filename)


class UploadService(object):

    def __init__(self, removal_service):
	self.removal_service = removal_service

    def upload_complete(self, filename):
	self.removal_service.rm(filename)
