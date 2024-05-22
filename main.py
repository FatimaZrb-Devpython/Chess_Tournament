import sys
sys.path.append(".")

from controllers.tournament  import TournamentController
from controllers.round import RoundController
from view.player import PlayerView

def main():
    # Utilisation du contrôleur pour ajouter un tournoi
    tournament_controller = TournamentController()
    print("Ajout d'un tournoi :")
    tournament_data = tournament_controller.tournament_view.get_tournament_input()
    new_tournament = tournament_controller.add_tournament(*tournament_data)

    # Obtenez la liste des joueurs
    player_view = PlayerView()
    players = player_view.get_players_input()

    # Enregistrer les joueurs dans le tournoi
    for player in players:
        new_tournament.register_player(player)

    # Créer les rounds et les matches pour le tournoi
    round_controller = RoundController()
    round_controller.create_rounds_and_matches(new_tournament, players)

if __name__ == "__main__":
    main()
