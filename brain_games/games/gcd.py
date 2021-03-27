from random import randint

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


def generate_round():
    number1 = randint(2, 100)
    number2 = randint(2, 100)
    question = '{} {}'.format(number1, number2)
    gcd = get_gcd(number1, number2)
    current_answer = str(gcd)
    return question, current_answer
