import random
from Utils import clear_screen

def play_guess_game(difficulty):
    secret_number = random.randint(1,difficulty)
    while True:
        try:
            guess = int(input('Please enter guess leve: '))

            if 0 <= guess <= difficulty:
                if guess == secret_number:
                    print('you Win')
                    return True
                else:
                    print(f'Try again , the number was {secret_number}')
                    return False
            else:
                print('You chose a number out of range')
            play_again = input('Do you want to play again Guess Game? y/n : ')
            if play_again.lower() != 'y':
                print('Thank you for playing')
                clear_screen()
                break
            else:
                print('Starting new Guess game ......')
                play_guess_game(difficulty)
        except ValueError:
            print('please enter a valid number')