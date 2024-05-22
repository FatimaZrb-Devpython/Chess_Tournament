import sys
sys.path.append("..")


from view.player import PlayerView
from models.tournament import ChessTournament
class TournamentView:
    def __init__(self):
        self.tournament = ChessTournament()
        self.player_view = PlayerView()

    def display_tournament_info(self):
        if self.tournament is None:
            print("No tournament information available.")
            return

        print(f"Tournament: {self.tournament.name}")
        print(f"Location: {self.tournament.location}")
        print(f"Start Date: {self.tournament.start_date}")
        print(f"End Date: {self.tournament.end_date}")
        print(f"Description: {self.tournament.description}")
        print("Registered Players:")
        for player in self.tournament.registered_players:
            print(f"- {player.first_name} {player.last_name}")

    def get_tournament_input(self):
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")
        start_date = input("Enter tournament start date (YYYY-MM-DD): ")
        end_date = input("Enter tournament end date (YYYY-MM-DD): ")
        description = input("Enter tournament description: ")
        return name, location, start_date, end_date, description

    def get_players_input(self):
        return self.player_view.get_players_input()
