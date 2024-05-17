import os
import json
import sys
sys.path.append("..")

from view.tournament import TournamentView
from models.tournament import ChessTournament

class TournamentController:
    def __init__(self):
        self.tournaments_folder = "tournaments/"
        os.makedirs(self.tournaments_folder, exist_ok=True)
        self.tournament_view = TournamentView()

    def add_tournament(self, name, location, start_date, end_date, description):
        tournament = ChessTournament(name, location, start_date, end_date, description=description)
        tournament_filename = f"{self.tournaments_folder}/{tournament.name.replace(' ', '_').lower()}.json"
        with open(tournament_filename, "w") as file:
            json.dump(tournament.to_dict(), file)
        print(f"Tournoi enregistré dans {tournament_filename}")
    
    
    
        
        