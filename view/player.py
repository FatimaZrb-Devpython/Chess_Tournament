class PlayerView:
    def __init__(self, player):
        self.player = player

    def display_player_info(self):
        print("Player Information:")
        print(f"First Name: {self.player.first_name}")
        print(f"Last Name: {self.player.last_name}")
        print(f"Date of Birth: {self.player.date_of_birth}")
        
    def get_player_input(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        return first_name, last_name, date_of_birth