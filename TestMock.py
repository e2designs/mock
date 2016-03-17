#!/usr/bin/python

from rmmodule import rm

import mock
import unittest
import pytest

class RmTestCase(unittest.TestCase):

    @mock.patch('rmmodule.os')
    def test_rm(self, mock_os):
	rm("any path")
	# Test that rm called os.remove with right parameters
	mock_os.remove.assert_called_with("any path")
