class Match:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.scores = {player1: 0, player2: 0}

    def set_winner(self, winner):
        loser = next(player for player in self.players if player != winner)
        self.scores[winner] = 1
        self.scores[loser] = 0

    def set_draw(self):
        for player in self.players:
            self.scores[player] = 0.5