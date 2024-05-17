from controllers.tournament import TournamentController
from controllers.round import RoundController

def main():
    tournament_controller = TournamentController()
    print("Ajout d'un tournoi :")
    tournament_data = tournament_controller.tournament_view.get_tournament_input()
    new_tournament = tournament_controller.add_tournament(*tournament_data)
    
    players = tournament_controller.tournament_view.get_players_input()
    for player in players:
        new_tournament.register_player(player)
    
    round_controller = RoundController(new_tournament)
    round_controller.create_rounds_and_matches(players)

if __name__ == "__main__":
    main()
