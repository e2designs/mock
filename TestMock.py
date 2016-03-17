#!/usr/bin/env python

from rmmodule import RemovalService as RS

import mock
import unittest
import pytest

class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch('rmmodule.os.path')
    @mock.patch('rmmodule.os')
    def test_rm(self, mock_os, mock_path):
	print mock_os
	print mock_path
	# Instantiate the service
	ref = RS()

	# Set up the mock
	mock_path.isfile.return_value = False

	ref.rm('anypath')
	
	# Test that the remove calls was NOT called
	self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

	# Make the file 'exist'
	mock_path.isfile.return_value = True

	ref.rm('anypath')

	# Test that rm called os.remove with right parameters
	mock_os.remove.assert_called_with('anypath')
