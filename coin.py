import random as rd

# Toss two coins at once
def toss_coins():
    return rd.choice(['H', 'T']), rd.choice(['H', 'T'])

# Display result of the toss
def display_results(coin1, coin2):
    print(f"Coin 1: {coin1}")
    print(f"Coin 2: {coin2}")

    if coin1 == coin2:
        print(" It's a match!")
    else:
        print(" No match, try again!")

# Ask the user to continue
def ask_continue():
    while True:
        response = input('Do you want to continue? (y/n): ').strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print('Invalid input, please enter "y" or "n".')

# Main game function
def play_game():
    print("Welcome to the Coin Toss Game!")

    while True:
        input("\nPress Enter to toss the coins...")

        coin1, coin2 = toss_coins()
        display_results(coin1, coin2)

        if not ask_continue():
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
