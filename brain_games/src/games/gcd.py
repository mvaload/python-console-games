from random import randint
from brain_games.src.engine import COUNT_ROUND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    a = num1
    b = num2

    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a + b


def run_game():
    data = []
    i = 0

    while i < COUNT_ROUND:
        number1 = randint(2, 100)
        number2 = randint(2, 100)
        question = '{} {}'.format(number1, number2)
        result = get_gcd(number1, number2)
        current_answer = str(result)
        data.append({'question': question, 'current_answer': current_answer})
        i += 1
    return data
