from random import randint
from math import sqrt
from brain_games.src.engine import COUNT_ROUND

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False

    limit = sqrt(num)
    i = 2

    while i <= limit:
        if num % i == 0:
            return False
        i += 1

    return True


def run_game():
    data = []
    i = 0

    while i < COUNT_ROUND:
        number = randint(2, 100)
        current_answer = is_prime(number)
        data.append({'question': number, 'current_answer': current_answer})
        i += 1
    return data
