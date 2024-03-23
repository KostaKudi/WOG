import random
import requests
from selenium.webdriver.common.keys import Keys as  Keys
from selenium.webdriver.common.by import By
from forex_python.converter import CurrencyRates
from Utils import clear_screen

def get_exchange_rate():
    try:
        response = requests.get('https://open.er-api.com/v6/latest/USD')
        data = response.json()
        return data['rates']['ILS']
    except Exception as e:
        print(f"Error: {e}")

exchange_rate = get_exchange_rate()
print("Exchange rate from USD to ILS:", exchange_rate)

def guess():
    return int(input('Please choose a guess: '))

def secret_number(difficlty,exchange_rate):
    exchange = exchange_rate
    random_number = random.randint(1, difficlty)
    return random_number * exchange

def low_limit(guess, secret_number):
    low_limt = 10 - guess
    return secret_number - low_limt

def high_limit(guess, secret_number):
    high_limit = 10 - guess
    return secret_number + high_limit


def play(low_limit, high_limit, guess):
    if low_limit <= guess <= high_limit:
        print('Great')
        return True
    else:
        print('Incorrect answer')
        return False

def play_currency_roulette_game(difficulty_level,exchange_rate):
    secret_number_value = secret_number(difficulty_level, exchange_rate)
    guess_number = guess()
    low = low_limit(guess_number, secret_number_value)
    high = high_limit(guess_number, secret_number_value)
    while True:
        if play(low, high, guess_number):
            play_again = input('Do you want to play again Currency Roulette game? y/n ')
            if play_again.lower() != 'y':
                print('Thank you for playing Currency Roulette game')
                clear_screen()
                break
            else:
                print('starting new Currency Roulette game....')
                play_currency_roulette_game()
        else:
            play_currency_roulette_game(difficulty_level)