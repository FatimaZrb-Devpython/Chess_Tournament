import sys
sys.path.append("..")

from view.player import Player
from controllers.player import PlayerController

class PlayerView:
    def __init__(self):
        self.player_controller = PlayerController()

    def get_player_input(self):
        first_name = input("Entrez le prénom du joueur: ")
        last_name = input("Entrez le nom de famille du joueur: ")
        date_of_birth = input("Entrez la date de naissance du joueur (YYYY-MM-DD): ")
        return first_name, last_name, date_of_birth

    def generate_player_json(self, file_path):
        first_name, last_name, date_of_birth = self.get_player_input()
        self.player_controller.generate_player_json(first_name, last_name, date_of_birth, file_path)

    

# Création d'une liste pour stocker les joueurs
players = []

# Création d'une instance de PlayerView pour gérer l'affichage et la saisie des informations du joueur
player_view = PlayerView(None)

# Demande à l'utilisateur de saisir les informations pour chaque joueur
num_players = int(input("Combien de joueurs souhaitez-vous ajouter ? "))
for i in range(num_players):
    print(f"\nJoueur {i+1}:")
    first_name, last_name, date_of_birth = player_view.get_player_input()
    player = Player(first_name, last_name, date_of_birth)
    players.append(player)

# Affichage des informations de chaque joueur en utilisant la méthode display_player_info de PlayerView
print("\nInformations des joueurs :")
for i, player in enumerate(players, start=1):
    print(f"\nJoueur {i}:")
    player_view.player = player  # Définir le joueur actuel pour l'affichage
    player_view.display_player_info()