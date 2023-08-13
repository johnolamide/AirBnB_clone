import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """
        """
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            content = f.read()
            key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
            self.assertIn(key, content)

    def test_reload(self):
        """ Test for the reload() method
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()
