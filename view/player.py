import sys
sys.path.append("..")

from models.player import Player
from controllers.player import PlayerController

class PlayerView:
    def __init__(self):
        self.player_controller = PlayerController()

    def get_player_input(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        return first_name, last_name, date_of_birth

    def get_players_input(self):
        players = []
        num_players = int(input("Combien de joueurs souhaitez-vous ajouter ? "))
        for i in range(num_players):
            print(f"\nJoueur {i+1}:")
            first_name, last_name, date_of_birth = self.get_player_input()
            player = Player(first_name, last_name, date_of_birth)
            players.append(player)
        return players
    

# Création d'une liste pour stocker les joueurs
# players = []

# # Création d'une instance de PlayerView pour gérer l'affichage et la saisie des informations du joueur
# player_view = PlayerView(None)

# # Demande à l'utilisateur de saisir les informations pour chaque joueur
# num_players = int(input("Combien de joueurs souhaitez-vous ajouter ? "))
# for i in range(num_players):
#     print(f"\nJoueur {i+1}:")
#     first_name, last_name, date_of_birth = player_view.get_player_input()
#     player = Player(first_name, last_name, date_of_birth)
#     players.append(player)

# # Affichage des informations de chaque joueur en utilisant la méthode display_player_info de PlayerView
# print("\nInformations des joueurs :")
# for i, player in enumerate(players, start=1):
#     print(f"\nJoueur {i}:")
#     player_view.player = player  # Définir le joueur actuel pour l'affichage
#     player_view.display_player_info()