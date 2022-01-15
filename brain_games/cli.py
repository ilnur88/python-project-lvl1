import prompt


def welcome_user():
    print('Welcome to Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
