import prompt
import random


def check_number_is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def generate_random_number():
    num = random.randint(1, 100)
    return num


def has_win_even_game():
    i = 0
    while i < 3:
        num = generate_random_number()
        print('Question: {}'.format(num))
        answer = prompt.string('Your answer: ')
        correct_answer = check_number_is_even(num)
        if answer == correct_answer:
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'".format(answer, correct_answer))
            return False
        i = i + 1
    return True


def even_game():
    print('Welcome to Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if has_win_even_game():
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))
