#!/usr/bin/python

from rmmodule import rm

import mock
import unittest
import pytest

class RmTestCase(unittest.TestCase):

    @mock.patch('rmmodule.os.path')
    @mock.patch('rmmodule.os')
    def test_rm(self, mock_os, mock_path):
	# Set up the mock
	mock_path.isfile.return_value = False

	rm("any path")
	
	# Test that the remove calls was NOT called
	self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

	# Make the file 'exist'
	mock_path.isfile.return_value = True

	rm("any path")

	# Test that rm called os.remove with right parameters
	mock_os.remove.assert_called_with("any path")
