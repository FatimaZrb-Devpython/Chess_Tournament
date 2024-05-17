from models.round import Round

class ChessTournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.description = description
        self.rounds = []
        self.registered_players = []

    def add_round(self, round_name):
        round_instance = Round(round_name)
        self.rounds.append(round_instance)

    def register_player(self, player):
        self.registered_players.append(player)

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "description": self.description,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "registered_players": [player.to_dict() for player in self.registered_players]
        }

    def update_scores(self):
        # Mettre à jour les scores totaux des joueurs
        for round_ in self.rounds:
            for match in round_.matches:
                for player, score in match.scores.items():
                    player.score += score