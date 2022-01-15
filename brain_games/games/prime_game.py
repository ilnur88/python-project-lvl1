import brain_games.games.games_universal as games


def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return 'no'
        i = i + 1
    return 'yes'


def has_win_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < games.ROUND_COUNT:
        num = games.generate_random_number()
        answer = games.get_answer('{}'.format(num))
        correct_answer = is_prime(num)
        if not games.is_answer_correct(answer, str(correct_answer)):
            return False
        i = i + 1
    return True
