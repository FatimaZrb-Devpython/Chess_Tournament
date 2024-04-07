class RoundView:
    def display_round_info(self):
        if self.round_instance is None:
            print("No round information available.")
            return

        print(f"Round: {self.round_instance.name}")
        print(f"Start Date and Time: {self.round_instance.start_datetime}")
        print(f"End Date and Time: {self.round_instance.end_datetime}")
        print("Matches:")
        for match in self.round_instance.matches:
            print(f"- {match.players[0].first_name} vs {match.players[1].first_name}")
            
    def get_round_input(self):
        round = input("Enter round: ")
        start_date_and_time = input("Enter Start Date and Time: ")
        end_date_and_time = input("Enter End Date and Time: ")
        return round, start_date_and_time, end_date_and_time