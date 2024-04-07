import json


class Player:
    """Player"""

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth 
        
    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth
        }

    # def save_to_json(self, file_path):
    #     with open(file_path, "w") as file:
    #         json.dump(self.to_dict(), file)

    # @classmethod
    # def load_from_json(cls, file_path):
    #     with open(file_path, "r") as file:
    #         data = json.load(file)
    #         return cls(**data)





