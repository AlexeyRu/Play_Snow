def most_frequent_characters(text):
    '''
    search for the most frequent characters in text
    :param text:
    :return: list of characters
    '''
    x = list(text)
    d = dict.fromkeys(set(x), 0)
    res = []
    for i in x:
        d[i] += 1
    for i in d:
        if d[i] == max(d.values()):
            res.append(i)
    return res


def sum_text_hole (text):
    '''
    Calculate number of text holes.
    :param text:
    :return: number of text holes
    '''
    x = list(text)
    res = 0
    for i in x:
        if i in list('qopadgb460QROPAD@'):
           res += 1
        elif i in list('8B%&'):
            res += 2
    return res


def is_palindrome (text) :
    '''
    Check if a text is palindrome or not
    :param text:
    :return: True or False
    '''
    if (text == text[::-1]):
        return True
    return False