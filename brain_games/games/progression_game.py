import brain_games.games.games_universal as games


def get_progression(begin, adder):
    length = games.random_number(10)
    if length < 5:
        length = 5
    hide_index = games.random_number(length)
    i = 1
    return_str = ''
    while i <= length:
        next_num = begin + adder * (i - 1)
        if i == hide_index:
            hide_num = next_num
            next_num = '..'
        return_str = '{} {}'.format(return_str, next_num)
        i = i + 1
    return (return_str.strip(), hide_num)


def has_win_game():
    print('What number is missing in the progression?')
    i = 0
    while i < games.ROUND_COUNT:
        begin = games.random_number(10)
        adder = games.random_number(10)
        (progress_str, hide_num) = get_progression(begin, adder)
        answer = games.get_answer('{}'.format(progress_str))
        if not games.is_answer_correct(answer, str(hide_num)):
            return False
        i = i + 1
    return True
