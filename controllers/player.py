import json
import sys
sys.path.append("..")

from models.player import Player

class PlayerController:
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def add_player(self, first_name, last_name, date_of_birth):
        player = Player(first_name, last_name, date_of_birth)
        self.player_repository.add_player(player)

    def generate_player_json(self, first_name, last_name, date_of_birth, file_path):
        player_data = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth
        }

        with open(file_path, "w") as file:
            json.dump(player_data, file)

    def get_all_players(self):
        return self.player_repository.get_all_players()