#!/usr/bin/python3
"""
A unit test module for the console (command interpreter).
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City


class TestHBNBCommand(unittest.TestCase):
    """
    Represents the test class for the HBNBCommand class.
    """
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """
        Tests the create command with the file storage.
        """
        cons = HBNBCommand()
        count = len(storage.all(City).keys())
        cons.onecmd('create City name="Texas"')
        count_1 = len(storage.all(City).keys())
        self.assertEqual(count_1, count + 1)
        # second test case
        count_2 = len(storage.all(City).keys())
        cons.onecmd('create City name="NewYork"')
        count_3 = len(storage.all(City).keys())
        self.assertEqual(count_3, count_2 + 1)
        # third test case
        counter = 0
        element_1 = None
        for element, value in storage.all(City).items():
            counter = counter + 1
            if counter == count_3:
                element_1 = value
        self.assertEqual('NewYork', element_1.__dict__["name"])
