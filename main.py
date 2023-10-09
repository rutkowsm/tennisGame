from easyAI import AI_Player, Negamax

class TennisGame:
    def __init__(self, player1, player2):
        self.ball_position = 0
        self.blue_points = 50
        self.red_points = 50
        self.players = [player1, player2]

    def get_bid(self, player_name, player_points):
        bid_awaiting = True
        while bid_awaiting:
            bid = int(input(f"{player_name}, enter points to deduct from your {player_points}: "))
            if bid < 0 or bid > player_points:
                print(f"Sorry, you need to set points between 0 and {player_points}")
            else:
                bid_awaiting = False
        return bid

    def move_ball(self, blue_bid, red_bid):
        if blue_bid == red_bid:
            new_position = self.ball_position
        elif blue_bid > red_bid and self.ball_position >= 0:
            new_position = -1
        elif red_bid > blue_bid and self.ball_position <= 0:
            new_position = 1
        elif blue_bid > red_bid and self.ball_position < 0:
            new_position = self.ball_position - 1
        else:
            new_position = self.ball_position + 1
        return new_position

    def play_game(self):
        game_on = True
        winner = ""
        while game_on:
            for i, player_name in enumerate(["Blue", "Red"]):
                if self.players[i] == "human":
                    bid = self.get_bid(player_name, self.blue_points if i == 0 else self.red_points)
                else:
                    bid = self.players[i].get_bid(self)

                self.ball_position = self.move_ball(bid, 0) if i == 0 else self.move_ball(0, bid)

                self.blue_points -= bid if i == 0 else 0
                self.red_points -= bid if i == 1 else 0

                print(f"Blue Score: {self.blue_points} points   Red Score: {self.red_points} points   Ball: {self.ball_position}")

                if self.blue_points <= 0 or self.red_points <= 0 or self.ball_position > 2 or self.ball_position < -2:
                    winner = "Red" if self.blue_points <= 0 or self.ball_position > 2 else "Blue"
                    game_on = False
                    break

        print(f"\nGame over! {winner} wins!")


class AIPlayer:
    def __init__(self, difficulty=3):
        self.AI = AI_Player(Negamax(difficulty))

    def get_bid(self, game):
        if game.ball_position == 0:
            return self.AI(game).choose_move()
        else:
            return 1  # Assuming the AI bids 1 point when ball position is not 0


def play_game():
    player1_type = int(input("Player 1: 1 for human, 2 for AI: "))
    player2_type = int(input("Player 2: 1 for human, 2 for AI: "))

    if player1_type == 1:
        player1 = "human"
    else:
        player1 = AIPlayer()

    if player2_type == 1:
        player2 = "human"
    else:
        player2 = AIPlayer()

    game = TennisGame(player1, player2)
    game.play_game()

# Start the game
play_game()
