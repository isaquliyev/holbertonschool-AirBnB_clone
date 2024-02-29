from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(TestCase):
    def setUp(self):
        self.fs = FileStorage()
        self.b1 = BaseModel()

    def test_class_attributes(self):
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_new(self):
        self.assertIn(self.b1, self.fs.all().values())
