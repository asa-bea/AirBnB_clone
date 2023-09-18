#!/usr/bin/python3

""" Unittest Test module for base_model module """

from models.base_model import BaseModel
import unittest
from datetime import datetime
import json
import os
import sys
import uuid


class TestBaseModel(unittest.TestCase):
    """ A TestCase class to test the Basemodel class """

    def test_init(self):
        """Test instantiation of BaseModel class"""

        model1 = BaseModel()
        self.assertIsInstance(model1, BaseModel)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
