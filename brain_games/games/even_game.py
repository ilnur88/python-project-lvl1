import brain_games.games.games_universal as games_universal


def check_number_is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def has_win_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < games_universal.ROUND_COUNT:
        num = games_universal.generate_random_number()
        answer = games_universal.get_answer(num)
        correct_answer = check_number_is_even(num)
        if not games_universal.is_answer_correct(answer, correct_answer):
            return False
        i = i + 1
    return True
