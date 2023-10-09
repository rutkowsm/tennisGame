from easyAI import TwoPlayerGame, AI_Player, Human_Player, Negamax


class Player():

    def __init__(self):
        self.points_left = 50
        self.player_name = None

    def make_move(self, bid):
        self.points_left -= bid


class TennisGame(TwoPlayerGame):
    def __init__(self, players=None):
        self.ball_position = 0
        self.players = players

    def possible_moves(self):
        moves = []
        for i in range(0, 51):
            moves.append(i)
        return moves

    def win(self):
        return self.ball_position == -3 or self.ball_position == 3

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def get_bid(self, player_name, points_left):
        bid_awaiting = True
        while bid_awaiting:
            bid = int(input(f"{player_name}, enter points to deduct from your {points_left}: "))
            if bid < 0 or bid > points_left:
                print(f"Sorry, you need to set points between 0 and {points_left}")
            else:
                bid_awaiting = False
        return bid


        # if blue_bid == red_bid:
        #     new_position = self.ball_position
        # elif blue_bid > red_bid and self.ball_position >= 0:
        #     new_position = -1
        # elif red_bid > blue_bid and self.ball_position <= 0:
        #     new_position = 1
        # elif blue_bid > red_bid and self.ball_position < 0:
        #     new_position = self.ball_position - 1
        # else:
        #     new_position = self.ball_position + 1
        #
        # return new_position

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

                print(
                    f"Blue Score: {self.blue_points} points   Red Score: {self.red_points} points   Ball: {self.ball_position}")

                if self.blue_points <= 0 or self.red_points <= 0 or self.ball_position > 2 or self.ball_position < -2:
                    winner = "Red" if self.blue_points <= 0 or self.ball_position > 2 else "Blue"
                    game_on = False
                    break

        print(f"\nGame over! {winner} wins!")


def play_game():
    ai = Negamax(10)
    game = TennisGame([AI_Player(ai), Human_Player()])
    game.play_game()


# Start the game
play_game()
