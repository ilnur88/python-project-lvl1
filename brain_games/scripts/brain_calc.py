#!/usr/bin/env python
from brain_games.games.calc_game import has_win_game
from brain_games.cli import welcome_user, get_name


def main():
    welcome_user()
    name = get_name()
    print('What is the result of the expression?')
    if has_win_game():
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
