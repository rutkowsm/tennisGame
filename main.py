import torch


class TennisAI:
    def __init__(self):
        self.name = "Blue"

    def get_bid(self, ball_position, player_points):
        if ball_position == 0:
            return min(player_points, 3)  # AI bids up to 3 points when ball is at center
        elif ball_position > 0:
            return min(player_points, 2)  # AI bids up to 2 points when ball is in opponent's court
        else:
            return 1  # AI bids 1 point when ball is in its own court

class Player:
    def __init__(self, name):
        self.name = name

    def get_bid(self, player_points):
        bid_awaiting = True
        while bid_awaiting:
            bid = int(input(f"{self.name}, enter points to deduct from your {player_points}: "))
            if bid < 0 or bid > player_points:
                print(f"Sorry, you need to set points between 0 and {player_points}")
            else:
                bid_awaiting = False
        return bid

class TennisGame:
    def __init__(self):
        self.ball_position = 0
        self.blue_points = 50
        self.red_points = 50
        self.ai_player = TennisAI()
        self.players = [self.ai_player, Player("Red")]

    def ai_get_bid(self):
        with torch.no_grad():
            input_data = torch.tensor([self.ball_position, self.blue_points], dtype=torch.float32)
            return int(round(self.ai_player(input_data).item()))

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
            # Blue (AI) makes a move
            blue_bid = self.players[0].get_bid(self.ball_position, self.blue_points)

            # Red (human) makes a move
            red_bid = self.players[1].get_bid(self.red_points)

            # Print current bids
            print(f"Blue bids: {blue_bid}   Red bids: {red_bid}")

            # Determine ball position and update scores
            self.ball_position = self.move_ball(blue_bid, red_bid)
            self.blue_points -= blue_bid
            self.red_points -= red_bid

            # Print current scores and ball position
            print(
                f"Blue Score: {self.blue_points} points   Red Score: {self.red_points} points   Ball: {self.ball_position}")

            # Check if game is over
            if self.blue_points <= 0 or self.red_points <= 0 or self.ball_position > 2 or self.ball_position < -2:
                winner = "Red" if self.blue_points <= 0 or self.ball_position > 2 else "Blue"
                game_on = False

        print(f"\nGame over! {winner} wins!")

def play_game():
    game = TennisGame()
    game.play_game()

# Start the game
play_game()
