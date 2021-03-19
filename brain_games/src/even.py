import prompt
from random import randint

COUNT_ROUND = 3


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def run():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < COUNT_ROUND:
        number = randint(2, 100)
        current_answer = is_even(number)
        print('Question: {}'.format(number))
        user_answer = prompt.string('Your answer: ')

        if current_answer != user_answer:
            template = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(template.format(user_answer, current_answer))
            print("Let's try again, Bill!")
            return

        print('Correct!')
        i += 1
    print('Congratulations, {}!'.format(user_name))
