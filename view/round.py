import sys
sys.path.append("..")

from models.round import Round

class RoundView:
    def __init__ (self):
        self.round_instance = Round()

    def display_round_info(self):
        if self.round_instance is None:
            print("Aucune information sur le tour disponible.")
            return

        print(f"Round: {self.round_instance.name}")
        print(f"Date et heure de début: {self.round_instance.start_datetime}")
        print(f"Date et heure de fin: {self.round_instance.end_datetime}")
        print("Matches:")
        for match in self.round_instance.matches:
            print(f"- {match.player[0].first_name} vs {match.player[1].first_name}")
            
    def get_round_input(self):
        round = input("Entrez le round: ")
        start_date_and_time = input("Entrez la date et l'heure de début: ")
        end_date_and_time = input("Entrez la date et l'heure de fin: ")
        return round, start_date_and_time, end_date_and_time