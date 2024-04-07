import json
import os 

# from datetime import datetime

from player import Player
from round import Round

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

    # def save_to_json(self, name, file_path):
    #     # Construire le chemin du dossier de la catégorie
    #     category_folder = rf"./tournament/"

    #     # Créer le dossier de la catégorie s'il n'existe pas
    #     os.makedirs(category_folder, exist_ok=True)

    #     # Construire le chemin du fichier dans le dossier de la catégorie
    #     file_path = os.path.join(category_folder, f"{name}.json")

    #     with open(file_path, "w") as file:
    #         json.dump(self.to_dict(), file)

    # @classmethod
    # def load_from_json(cls, file_path):
    #     with open(file_path, "r") as file:
    #         data = json.load(file)
    #         tournament = cls(data["name"], data["location"], data["start_date"], data["end_date"],
    #                          data["num_rounds"], data["current_round"], data["description"])
    #         tournament.rounds = [Round.from_dict(round_data) for round_data in data["rounds"]]
    #         tournament.registered_players = [Player(**player_data) for player_data in data["registered_players"]]
    #         return tournament



