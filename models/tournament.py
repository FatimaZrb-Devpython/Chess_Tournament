from datetime import datetime

from models.match import *



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
        round_instance = TournamentRound(round_name)
        self.rounds.append(round_instance)

    def register_player(self, player):
        self.registered_players.append(player)


class TournamentRound:
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