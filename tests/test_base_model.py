#!/usr/bin/python3
""" Module contains the test class for the BaseModel Class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def tearDown(self):
        """
        """
        del self.bm1
        del self.bm2

    def test_init(self):
        """
        """
        self.assertIsInstance(self.bm1.id, str)
        self.assertIsInstance(self.bm2.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.created_at, datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime)

    def test_str(self):
        """
        """
        expected_str = "[BaseModel] ({}) {}".format(self.bm1.id, self.bm1.__dict__)
        self.assertEqual(str(self.bm1), expected_str)

    def test_save(self):
        """
        """
        old_updated_at = self.bm1.updated_at
        self.bm1.save()
        self.assertNotEqual(old_updated_at, self.bm1.updated_at)

    def test_to_dict(self):
        """
        """
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict, dict)
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(bm1_dict["created_at"], self.bm1.created_at.isoformat())
        self.assertEqual(bm1_dict["updated_at"], self.bm1.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
