from Games.memory_game import play_memory_game
from Games.currency_roulette_game import play_currency_roulette_game
from Games.guess_game import play_guess_game
import os

from Utils import add_score, clear_screen
def welcome():
    name = input('What is your name: ')
    print(f'Hi {name} and welcome to the World of Games: The Epic Journey')
    file = open('scores.txt', 'a')
    file.write(name + '\n')

def start_play():
    def get_valid_input(prompt, valid_range):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input in valid_range:
                    return user_input
                else:
                    print(f'Invalid input. Please select a number between {valid_range[0]} and {valid_range[-1]}.')
            else:
                print('Invalid input. Please enter a number.')

    while True:
        print('Please Choose a game to play: '
              '\n1. Memory Game'
              '\n2. Guess Game'
              '\n3. Currency Roulette')

        game = get_valid_input('Your choice: ', [1, 2, 3])

        games = {1: 'Memory Game', 2: 'Guess Game', 3: 'Currency Roulette'}
        print(games[game])

        while True:
            difficulty = get_valid_input('Please Choose difficulty between 1 - 3: ', [1, 2, 3])
            # Assume play_choosen_game returns True if the user won the game, False otherwise
            if play_choosen_game(game, difficulty):
                # Call add_score function if user won the game
                add_score(difficulty)

            play_again = input('Do you want to play again a different game? (y/n)')
            if play_again.lower() != 'y':
                # Clear the screen before starting a new game
                clear_screen()


def play_choosen_game(select_game,selected_difficulty):
    game_functions = {
        1: play_memory_game,
        2: play_guess_game,
        3: play_currency_roulette_game
    }
    while True:
        if select_game in game_functions:
            game_functions[select_game](selected_difficulty)

        play_again = input('Do you want to play again a different game?  (y/n) ')
        if play_again.lower() != 'y':
            clear_screen()
        else:
            start_play()