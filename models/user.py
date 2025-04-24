from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, **kwargs):
    #     """
    #     Initialize a user instance
    #     """
    #     super().__init__(**kwargs)