import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up a user instance for testing
        """
        self.user = User()
    def tearDown(self):
        """delete created object"""
        del self.user

    def test_user_inherits_from_base_model(self):
        """
        Test that User class inherits from BaseModel
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """
        Test that User class has the correct attributes
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))