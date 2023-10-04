def get_bids(blue_points, red_points):
    blue_bid_awaiting = True
    red_bid_awaiting = True
    blue_bid = 0
    red_bid = 0
    while blue_bid_awaiting:
        # Blue player's initial move
        blue_bid = int(input(f"Blue, enter points to deduct from your {blue_points}: "))
        if blue_bid < 0 or blue_bid > blue_points:
            print(f"Sorry, you need to set points between 0 and {blue_points}")
        else:
            blue_bid_awaiting = False
    while red_bid_awaiting:
        # Red player's initial move
        red_bid = int(input(f"Red, enter points to deduct from your {red_points}: "))
        if red_bid < 0 or red_bid > red_points:
            print(f"Sorry, you need to set points between 0 and {red_points}")
        else:
            red_bid_awaiting = False

    return blue_bid, red_bid


def move_ball(ball_position, blue_bid, red_bid):
    if blue_bid == red_bid:
        new_position = ball_position
    elif blue_bid > red_bid and ball_position >= 0:
        new_position = -1
    elif red_bid > blue_bid and ball_position <= 0:
        new_position = 1
    elif blue_bid > red_bid and ball_position < 0:
        new_position = ball_position - 1
    else:
        new_position = ball_position + 1

    return new_position


def play_game():
    # Get initial moves
    ball_position = 0
    blue_points = 50
    red_points = 50
    game_on = True
    winner = ""
    while game_on:
        blue_bid, red_bid = get_bids(blue_points, red_points)
        # Print current scores and ball position

        ball_position = move_ball(ball_position, blue_bid, red_bid)
        blue_points = blue_points - blue_bid
        red_points = red_points - red_bid

        print(
            f"Blue Score: {blue_points} points   Red Score: {red_points} points   Ball: {ball_position}")

        # Check if game is over
        if blue_points <= 0 or ball_position > 2:
            winner = "Red"
            game_on = False
        elif red_points <= 0 or ball_position < -2:
            winner = "Blue"
            game_on = False

    print(f"\nGame over! {winner} wins!")


# Start the game
play_game()
