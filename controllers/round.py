import random
import json
import os
import sys
sys.path.append("..")

from datetime import datetime

from models.round import Round
from models.match import Match

class RoundController:
    def __init__(self, tournament):
        self.tournament = tournament
        self.tournaments_folder = "tournaments/"
        os.makedirs(self.tournaments_folder, exist_ok=True)

    def create_rounds_and_matches(self, players):
        if len(players) < 4:
            print("Pas assez de joueurs pour créer les rounds et les matches.")
            return

        num_rounds = 4
        random.shuffle(players)
        played_matches = set()

        for round_num in range(1, num_rounds + 1):
            round_name = f"Round {round_num}"
            round_instance = Round(round_name)
            self.tournament.add_round(round_instance)
            matches_per_round = []

            available_players = players[:]
            while len(available_players) > 1:
                player1 = available_players.pop(0)
                for i, player2 in enumerate(available_players):
                    if (player1, player2) not in played_matches and (player2, player1) not in played_matches:
                        played_matches.add((player1, player2))
                        matches_per_round.append(Match(player1, player2))
                        available_players.pop(i)
                        break

            round_instance.matches = matches_per_round
            round_instance.start_round()
            self.save_tournament()
            round_instance.end_round()
            self.save_tournament()
        
        top_players = sorted(players, key=lambda p: p.score, reverse=True)[:2]
        final_round_name = f"Round {num_rounds + 1}"
        final_round_instance = Round(final_round_name)
        final_match = Match(top_players[0], top_players[1])
        final_round_instance.matches.append(final_match)
        self.tournament.add_round(final_round_instance)
        self.save_tournament()

    def save_tournament(self):
        tournament_filename = f"{self.tournaments_folder}/{self.tournament.name.replace(' ', '_').lower()}.json"
        with open(tournament_filename, "w") as file:
            json.dump(self.tournament.to_dict(), file)
        print(f"Tournoi mis à jour dans {tournament_filename}")
