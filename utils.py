import os

from app import start_play
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 7

POINTS_OF_WINNING = (start_play() * 3) + 5
SCORES_FILE = "scores.txt"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def add_score(difficulty):
    try:
        with open(SCORES_FILE, "r") as file:
            current_score = int(file.read().strip())
    except FileNotFoundError:
        current_score = 0
    new_score = current_score + POINTS_OF_WINNING(difficulty)
    with open(SCORES_FILE, "w") as file:
        file.write(str(new_score))

    return new_score