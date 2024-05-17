class TournamentView:
    def __init__(self, tournament=None, round_instance=None):
        self.tournament = tournament
        self.round_instance = round_instance

    def display_tournament_info(self):
        if self.tournament is None:
            print("Aucune information sur le tournoi disponible.")
            return

        print(f"Tournoi: {self.tournament.name}")
        print(f"Lieu: {self.tournament.location}")
        print(f"Date de début: {self.tournament.start_date}")
        print(f"Date de fin: {self.tournament.end_date}")
        print(f"Description: {self.tournament.description}")
        print("Joueurs inscrits:")
        for player in self.tournament.registered_players:
            print(f"- {player.first_name} {player.last_name}")
            
    def get_tournament_input(self):
        tournament = input("Entrez le nom du tournoi: ")
        location = input("Entrez le lieu: ")
        start_date = input("Entrez la date de début: ")
        end_date = input("Entrez la date de fin: ")
        description = input("Description: ")
        return tournament, location, start_date, end_date, description
      