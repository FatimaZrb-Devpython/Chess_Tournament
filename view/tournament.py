class TournamentView:
    def __init__(self, tournament=None, round_instance=None):
        self.tournament = tournament
        self.round_instance = round_instance

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
        tournament = input("Enter Name of Tournament: ")
        location = input("Enter Location: ")
        start_date = input("Enter Start Date: ")
        end_date = input("Enter End Date: ")
        description = input("Description: ")
        return tournament, location, start_date,end_date,description
    

            