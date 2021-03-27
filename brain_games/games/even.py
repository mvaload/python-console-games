from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = randint(2, 100)
    current_answer = 'yes' if is_even(question) else 'no'
    return str(question), current_answer
