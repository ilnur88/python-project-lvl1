import brain_games.games.games_universal as games


def get_gcd(num1, num2):
    if num1 > num2:
        big_num = num1
        small_num = num2
    else:
        big_num = num2
        small_num = num1
    
    if big_num % small_num == 0:
        return small_num
    
    i = small_num // 2
    while i > 0:
        if big_num % i == 0 and small_num % i == 0:
            return i
        i = i - 1


def has_win_game():
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < games.ROUND_COUNT:
        num1 = games.generate_random_number()
        num2 = games.generate_random_number()        
        answer = games.get_answer('{} {}'.format(num1, num2))
        correct_answer = get_gcd(num1, num2)
        if not games.is_answer_correct(answer, str(correct_answer)):
            return False
        i = i + 1
    return True
