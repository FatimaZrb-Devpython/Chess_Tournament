import sys
sys.path.append("..")


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.scores = {player1: 0, player2: 0}

    def to_dict(self):
        return {
            "player1": self.player1.to_dict(),
            "player2": self.player2.to_dict(),
            "scores": {player.first_name: score for player, score in self.scores.items()}
        }

    def set_score(self, player, score):
        if player in self.scores:
            self.scores[player] = score





# # Récupérez les deux premiers joueurs de la liste pour tester la classe Match
# player1, player2 = players[:2]

# # Utilisez ces instances pour créer une instance de la classe Match avec des scores initiaux
# match = Match(player1, player2, score_player1=1, score_player2=0)

# # Utilisez la méthode to_dict() pour obtenir les informations du match sous forme de dictionnaire
# match_info = match.to_dict()

# # Affichez les informations du match
# print("Informations du match :")
# print("Joueurs :")
# for player_info in match_info["players"]:
#     print(f"  Nom : {player_info['last_name']} {player_info['first_name']}")
# print("Scores :")
# for player, score in match_info["scores"].items():
#     print(f"  {player.first_name} {player.last_name} : {score}")