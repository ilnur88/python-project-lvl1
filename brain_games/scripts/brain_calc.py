#!/usr/bin/env python
from brain_games.games.calc_game import has_win_game
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    if has_win_game():
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
