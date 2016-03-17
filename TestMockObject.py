#!/usr/bin/env python

from rmmodule import RemovalService, UploadService

import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):

    @mock.patch('rmmodule.os.path')
    @mock.patch('rmmodule.os')
    def test_rm(self, mock_os, mock_path):
	# Instantiate the service
	ref = RemovalService()

	# Set up the mock
	mock_path.isfile.return_value = False

	ref.rm("any path")

	# Test that remove call was NOT called. 
	self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

	# Make the file 'exist'
	mock_path.isfile.return_value = True

	ref.rm("any path")

	mock_os.remove.assert_called_with("any path")

class UploadServiceTestCase(unittest.TestCase):

    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
	# Build dependencies
	removal_service = RemovalService()
	reference = UploadService(removal_service)

	# Call upload_complete, which should call rm
	mock_rm.assert_called_with("My uploaded file")

	# Check that rm method was called
	removal_service.rm.assert_called_with("My uploaded file")
