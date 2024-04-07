import json 
import os
from player import Player

class Match:
    
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.scores = {player1: 0, player2: 0}

    def set_winner(self, winner):
        loser = next(player for player in self.players if player != winner)
        self.scores[winner] = 1
        self.scores[loser] = 0

    def set_draw(self):
        for player in self.players:
            self.scores[player] = 0.5

    def to_dict(self):
        return {
            "players": [player.to_dict() for player in self.players],
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        player1 = Player(**data["players"][0])
        player2 = Player(**data["players"][1])
        match = cls(player1, player2)
        match.scores = data["scores"]
        return match

    def save_to_json(self, name):
        # Construire le chemin du dossier de la catégorie
        category_folder = "./tournament/"

        # Créer le dossier de la catégorie s'il n'existe pas
        os.makedirs(category_folder, exist_ok=True)

        # Construire le chemin du fichier dans le dossier de la catégorie
        file_path = os.path.join(category_folder, f"{name}.json")
        with open(file_path, "w") as file:
            json.dump(self.to_dict(), file)
