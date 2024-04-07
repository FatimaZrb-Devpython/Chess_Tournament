import json

from datetime import datetime
from match import Match

class Round:
    """Round Progress"""

    def __init__(self, name):
        self.name = name
        self.start_datetime = None
        self.end_datetime = None
        self.matches = []

    def start_round(self):
        self.start_datetime = datetime.now()

    def end_round(self):
        self.end_datetime = datetime.now()

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)
        
    def to_dict(self):
        return {
            "name": self.name,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "matches": [match.to_dict() for match in self.matches]
        }

    # def save_to_json(self, file_path):
    #     with open(file_path, "w") as file:
    #         json.dump(self.to_dict(), file)

    # @classmethod
    # def from_dict(cls, data):
    #     round_ = cls(data["name"])
    #     round_.start_datetime = data["start_datetime"]
    #     round_.end_datetime = data["end_datetime"]
    #     round_.matches = [Match.from_dict(match_data) for match_data in data["matches"]]
    #     return round_