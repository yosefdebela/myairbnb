from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel:
    """
    the base model for all model isntances
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if 'created_at' in key or 'updated_at' in key:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:

            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)

    def to_dict(self):
        dic = {}
        dic['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        globals()['dic'] = dic
        return dic
    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save(self)
        







