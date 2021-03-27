from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def calculate(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2


def generate_round():
    operators = ['+', '-', '*']
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice(operators)
    question = '{} {} {}'.format(number1, operator, number2)
    calc_result = calculate(number1, number2, operator)
    current_answer = str(calc_result)
    return question, current_answer
