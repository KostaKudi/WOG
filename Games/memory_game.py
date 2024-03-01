import random
import time

from utils import clear_screen


def generate_numbers(difficulty):
    sequence = []
    for number in range(difficulty):
        sequence.append(random.randint(1,101))
    return sequence

def guess(sequence,difficulty):
    print('Please remember the following numbers, they will appear for 0.7 seconds')
    print(sequence)
    time.sleep(0.7)
    user_input = []

    for number in range(difficulty):
        while True:
            try:
                user_number = int(input(f'Enter number {number + 1}:'))
                user_input.append(user_number)
                break
            except:
                print('Enter valid number')
    return user_input

def compare_lists(sequence,user_input):
    if sequence == user_input:
        print('Congratulations, you won!')
        return True
    else:
        print('No Match '
              f'\nPlease try again')
        return False


def play_memory_game(difficulty_level):
    while True:
        sequence = generate_numbers(difficulty_level)
        user_guess = guess(sequence, difficulty_level)
        if compare_lists(sequence, user_guess):
            play_again = input('Do you want to play again Memory game? (y/n): ')
            if play_again.lower() != 'y':
                print('Thanks for playing! Exiting the game.')
                clear_screen()
                break
            else:
                print('Starting a new round...')
        else:
            print('You lost. Try again.')










