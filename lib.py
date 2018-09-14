def most_frequent_characters(text):
    """
    search for the most frequent characters in text
    :param text:
    :return: list of characters
    """
    x = list(text)
    d = dict.fromkeys(set(x), 0)
    res = []
    for i in x:
        d[i] += 1
    for i in d:
        if d[i] == max(d.values()):
            res.append(i)
    return res[0]


def sum_text_hole(text):
    """
    Calculate number of text holes.
    :param text:
    :return: number of text holes
    """
    res = 0
    for i in text:
        if i in 'qopadgb4690QROPAD@':
           res += 1
        elif i in '8B%&':
            res += 2
    return res


def is_palindrome(text):
    """
    Check if a text is palindrome or not
    :param text:
    :return: True or False
    """
    text = ''.join(text.strip().lower().split())
    return text == text[::-1]


def find_winner(game_state):
    """
    Determination of the winner in the game of tic-tac-toe
    :param game_state:
    :return:'X' or 'O'
    """
    res2 = [0, 0, 0]
    res3 = 'D'
    res4, res5 = 0, 0
    for r, i in enumerate(game_state):
        res1 = 0
        for c, j in enumerate(i):
            if j == 'X':
                res1 += 1
                res2[c] += 1
            if r == 0 and c == 0 and j == 'X': res4 += 1
            if r == 0 and c == 2 and j == 'X': res5 += 1
            if r == 1 and c == 1 and j == 'X': res4 += 1; res5 += 1
            if r == 2 and c == 0 and j == 'X': res5 += 1
            if r == 2 and c == 2 and j == 'X': res4 += 1
            #print(res1, end="  ")
        #print(res3, res2, res4, res5, )
        if res1 == 0:
            res3 = 'O'
        elif res1 == 3:
            res3 = 'X'
    res = 'D'
    if res3 == 'O': res = 'O'
    elif res3 == 'X': res = 'X'
    else:
        if 0 in res2: res = 'O'
        elif 3 in res2: res = 'X'
        else:
            if res4 == 0 or res5 == 0: res = 'O'
            if res4 == 3 or res5 == 3: res = 'X'
    return res


def check_input_tictactoe_state(input):
    """
    Check input validation
    :param input: string which cconsist from 3 characters
    :return:validation - True/False, reason: string
    """
    validation = False
    if len(input) < 3 :
        reason = 'input is too short (need 3 symbols). Try one more time!'
    elif len(input) > 3 :
        reason = 'input is too long (need 3 symbols). Try one more time!'
    else:
        v = 1
        for j in [i in {'X', 'O','x','o'} for i in input]:
            v = v * j
        if  v == 1:
            validation = True
            reason = input.upper()
        else:
            reason = 'You use no correct symbols (only "X" and "O"). Try one more time!'
    return validation, reason


def most_frequent_word(text):
    """
    search for the most frequent words in text
    :param text: text in one string
    :return: first most frequent word
    """
    text = text.strip().lower().split()
    t = list(frozenset(text))
    v = [text.count(i) for i in t]
    return t[v.index(max(v))]

