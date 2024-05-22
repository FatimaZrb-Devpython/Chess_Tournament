import json
import sys
import random
sys.path.append("..")

from models.match import Match

class RoundController:
    def __init__(self):
        self.tournaments_folder = "tournaments/"
    
    def save_tournament(self, tournament):
        tournament_filename = f"{self.tournaments_folder}/{tournament.name.replace(' ', '_').lower()}.json"
        with open(tournament_filename, "w") as file:
            json.dump(tournament.to_dict(), file)
        print(f"Tournoi mis à jour dans {tournament_filename}")

    def create_rounds_and_matches(self, tournament, players):
        if len(players) < 4:
            print("Pas assez de joueurs pour créer les rounds et les matches.")
            return

        num_rounds = tournament.num_rounds
        all_matches = []

        # Création des rounds et des matches aléatoires sans répétition de confrontation
        for round_num in range(1, num_rounds):
            round_name = f"Round {round_num}"
            tournament.add_round(round_name)
            available_players = players[:]
            random.shuffle(available_players)
            matches = []

            while len(available_players) > 1:
                player1 = available_players.pop()
                player2 = available_players.pop()
                match = Match(player1, player2)
                matches.append(match)
                all_matches.append(match)

            tournament.rounds[-1].matches = matches
            self.save_tournament(tournament)

        # Dernier round avec les meilleurs joueurs
        round_name = f"Round {num_rounds}"
        tournament.add_round(round_name)
        sorted_players = sorted(players, key=lambda x: x.score, reverse=True)
        match = Match(sorted_players[0], sorted_players[1])
        tournament.rounds[-1].matches = [match]
        self.save_tournament(tournament)
