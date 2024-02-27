from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(TestCase):
    def setUp(self):
        self.b1 = BaseModel()
        self.created_at = self.b1.created_at.isoformat()
        self.updated_at = self.b1.updated_at.isoformat()

        self.b2 = BaseModel()

    def test_attributes(self):
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_str(self):
        result = "[{}] ({}) {}".format(BaseModel.__name__,
                                       self.b1.id,
                                       self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())

    def test_save(self):
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_to_dict(self):
        new_dict = self.b1.to_dict()

        self.assertEqual(new_dict['__class__'], BaseModel.__name__)
        self.assertEqual(new_dict['created_at'], self.created_at)
        self.assertEqual(new_dict['updated_at'], self.updated_at)
