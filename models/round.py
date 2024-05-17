from datetime import datetime
from models.match import Match

class Round:
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
