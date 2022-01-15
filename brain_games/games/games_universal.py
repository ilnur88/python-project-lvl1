import prompt
import random


ROUND_COUNT = 3
MAX_NUMBER = 100


def get_answer(s):
    print('Question: {}'.format(s))
    return prompt.string('Your answer: ')


def is_answer_correct(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("'{}' is wrong answer ;(. "
              "Correct answer was '{}'".format(answer, correct_answer))
        return False


def random_number(max):
    num = random.randint(1, max)
    return num


def generate_random_number():
    num = random.randint(1, MAX_NUMBER)
    return num
