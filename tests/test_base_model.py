#!/usr/bin/python3
""" Module contains the test class for the BaseModel Class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """

    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    date_string = "2023-08-08T20:19:01.686918"
    date_object = datetime.strptime(date_string, date_format)
    kwargs = {
        'id': '123456',
        'created_at': date_string,
        'updated_at': date_string,
        'name': 'test',
        'my_number': 89
    }

    def setUp(self):
        """
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        self.bm3 = BaseModel(**self.kwargs)

    def tearDown(self):
        """
        """
        del self.bm1
        del self.bm2
        del self.bm3

    def test_init_without_kwargs(self):
        """
        """
        self.assertIsInstance(self.bm1.id, str)
        self.assertIsInstance(self.bm2.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.created_at, datetime)
        self.assertIsInstance(self.bm1.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
        """
        self.assertEqual(self.bm3.id, '123456')
        self.assertEqual(self.bm3.name, 'test')
        self.assertEqual(self.bm3.my_number, 89)
        self.assertEqual(self.bm3.created_at, self.date_object)
        self.assertEqual(self.bm3.updated_at, self.date_object)

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
