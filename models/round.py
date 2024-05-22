from models.match import Match

class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []

    def to_dict(self):
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches]
        }

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)
