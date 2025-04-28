import json
import os
# from models.base_model import BaseModel

class FileStorage:
    pass
    __file_path = 'file.json'
    __objects = {} # will store objects ny class_name.id
    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self, new_obj=None):
        """
        save will save the file in to a json file available locally
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = new_obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f, indent=4)


    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    self.__objects = json.load(f)
                except json.JSONDecodeError:
                    pass
