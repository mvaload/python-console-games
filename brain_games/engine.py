import prompt

COUNT_ROUND = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    description = game.DESCRIPTION
    print(description)

    count = COUNT_ROUND

    while count:
        question, current_answer = game.generate_round()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')

        if current_answer != user_answer:
            template = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(template.format(user_answer, current_answer))
            print("Let's try again, {}!".format(user_name))
            return

        count -= 1
        print('Correct!')

    print('Congratulations, {}!'.format(user_name))
