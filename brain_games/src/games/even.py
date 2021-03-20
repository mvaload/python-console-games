from random import randint
from brain_games.src.engine import COUNT_ROUND

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def run_game():
    data = []
    i = 0
    while i < COUNT_ROUND:
        number = randint(2, 100)
        current_answer = is_even(number)
        data.append({'question': number, 'current_answer': current_answer})
        i += 1
    return data
