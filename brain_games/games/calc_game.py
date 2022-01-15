import brain_games.games.games_universal as games


def get_random_operand(num):
    modulo = num % 3
    if modulo == 0:
        return '+'
    if modulo == 1:
        return '-'
    if modulo == 2:
        return '*'


def calc_values_with_operand(num1, num2, operand):
    if operand == '+':
        return num1 + num2
    if operand == '-':
        return num1 - num2
    if operand == '*':
        return num1 * num2


def has_win_game():
    print('What is the result of the expression?')
    i = 0
    while i < games.ROUND_COUNT:
        num1 = games.generate_random_number()
        num2 = games.generate_random_number()
        operand = get_random_operand(games.generate_random_number())
        answer = games.get_answer('{} {} {}'.format(num1, operand, num2))
        correct_answer = calc_values_with_operand(num1, num2, operand)
        if not games.is_answer_correct(answer, str(correct_answer)):
            return False
        i = i + 1
    return True
