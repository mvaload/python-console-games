from random import randint, choice
from brain_games.src.engine import COUNT_ROUND

DESCRIPTION = 'What is the result of the expression?'


def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2


def run_game():
    data = []
    i = 0
    operators = ['+', '-', '*']
    while i < COUNT_ROUND:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operator = choice(operators)
        question = '{} {} {}'.format(number1, operator, number2)
        calc_result = calculate(number1, number2, operator)
        current_answer = str(calc_result)
        data.append({'question': question, 'current_answer': current_answer})
        i += 1
    return data
