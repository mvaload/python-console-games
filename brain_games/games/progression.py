from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression(length, start, step):
    progression = []
    current_element = start

    while length:
        progression.append(current_element)
        current_element += step
        length -= 1
    return progression


def generate_round():
    progression_length = 10
    start = randint(0, 90)
    step = randint(2, 10)
    hidden_index_item = randint(0, progression_length - 1)
    progression = make_progression(progression_length, start, step)
    current_answer = str(progression[hidden_index_item])
    progression[hidden_index_item] = '..'
    question = ' '.join(str(element) for element in progression)
    return question, current_answer
