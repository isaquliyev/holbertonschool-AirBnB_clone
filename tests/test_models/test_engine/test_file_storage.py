from unittest import TestCase
from models.engine.file_storage import FileStorage

class TestFileStorage(TestCase):
    def setUp(self):
        self.fs = FileStorage()

    def test_class_attributes(self):
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)
