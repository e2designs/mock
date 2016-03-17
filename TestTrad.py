#!/usr/bin/python

from rmmodule import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
	with open(self.tmpfilepath, "wb") as f:
	    f.write("Delete me!")

    def test_rm(self):
	# Remove the file
	rm(self.tmpfilepath)

	# Test if it was actually removed
	self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")
