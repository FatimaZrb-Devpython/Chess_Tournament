import sys
sys.path.append("..")

from view.player import players  # Importez la liste de joueurs du fichier player.py

class Match:
    
    def __init__(self, player1, player2, score_player1=0, score_player2=0):
        self.players = [player1, player2]
        self.scores = {player1: score_player1, player2: score_player2}

    def set_winner(self, winner):
        loser = next(player for player in self.players if player != winner)
        self.scores[winner] += 1  # Mis à jour du score gagnant
        self.scores[loser] = 0    # Réinitialiser le score du perdant

    def set_draw(self):
        for player in self.players:
            self.scores[player] = 0.5

    def to_dict(self):
        return {
            "players": [player.to_dict() for player in self.players],
            "scores": self.scores
        }




# Récupérez les deux premiers joueurs de la liste pour tester la classe Match
player1, player2 = players[:2]

# Utilisez ces instances pour créer une instance de la classe Match avec des scores initiaux
match = Match(player1, player2, score_player1=1, score_player2=0)

# Utilisez la méthode to_dict() pour obtenir les informations du match sous forme de dictionnaire
match_info = match.to_dict()

# Affichez les informations du match
print("Informations du match :")
print("Joueurs :")
for player_info in match_info["players"]:
    print(f"  Nom : {player_info['last_name']} {player_info['first_name']}")
print("Scores :")
for player, score in match_info["scores"].items():
    print(f"  {player.first_name} {player.last_name} : {score}")