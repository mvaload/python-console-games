import prompt

COUNT_ROUND = 3


def run(game_data, description):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(description)

    for data in game_data:
        print('Question: {}'.format(data['question']))
        user_answer = prompt.string('Your answer: ')

        if data['current_answer'] != user_answer:
            template = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(template.format(user_answer, data['current_answer']))
            print("Let's try again, Bill!")
            return

        print('Correct!')

    print('Congratulations, {}!'.format(user_name))
