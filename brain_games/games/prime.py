from random import randint
from math import sqrt

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


def generate_round():
    question = randint(2, 100)
    current_answer = 'yes' if is_prime(question) else 'no'
    return str(question), current_answer
