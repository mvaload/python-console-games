from random import randint
from brain_games.src.engine import COUNT_ROUND

DESCRIPTION = 'What number is missing in the progression?'


def make_progression(length, start, step):
    progression = []
    start_element = start
    i = 0

    while i < length:
        progression[i] = start_element
        start_element += step
        i += 1
    return progression


def run_game():
    data = []
    i = 0
    progression_length = 10

    while i < COUNT_ROUND:
        start = randint(0, 90)
        step = randint(2, 10)
        hidden_element = randint(0, progression_length - 1)
        progression = make_progression(progression_length, start, step)
        current_answer = str(progression[hidden_element])
        progression[hidden_element] = '..'
        question = ' '.join(progression)
        data.append({'question': question, 'current_answer': current_answer})
        i += 1
    return data
