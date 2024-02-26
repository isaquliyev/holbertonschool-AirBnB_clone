#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from datetime import date


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        name = "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id,
                                     self.__dict__)
        return name

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict['__class__'] = BaseModel.__name__
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = self.__dict__[key].isoformat()
            else:
                new_dict[key] = self.__dict__[key]
        return new_dict
