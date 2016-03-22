#!/usr/bin/env python

from rmmodule import RemovalService as RS
from rmmodule import UploadService as US

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch('rmmodule.os.path')
    @mock.patch('rmmodule.os')
    def test_rm(self, mock_os, mock_path):
	# Instantiate the service.
	ref = RS()

	# Set up the mock
	mock_path.isfile.return_value = False

	ref.rm("any path")

	# Test that the remove call was NOT called.
	self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

	# Make the file 'exist'
	mock_path.isfile.return_value = True

	ref.rm("any path")

	mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):

    @mock.patch.object(RS, 'rm')
    def test_upload_complete(self, mock_rm):
	# Build the dependencies
	mock_removal_service = mock.create_autospec(RS)
	ref = US(mock_removal_service)

	# Call upload_complete, which should, in turn call 'rm'
	ref.upload_complete("my uploaded file")

	# Test that it called the rm method
	mock_removal_service.rm.assert_called_with("my uploaded file")

