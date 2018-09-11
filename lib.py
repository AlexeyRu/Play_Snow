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


def polyndrom (text, len_of_poly = 5) :
    '''
    search polyndroms in text
    :param text:
    :return: list of polyndroms or Null
    '''
    x = list(text)
    res = 'no polyndrom'

    if len(x) < len_of_poly-1:
        res = 'text too short'
    else:
        word = ''.join(x[0:(len_of_poly-1)])
        flag = False
        i = len_of_poly-2
        while flag == False:
            i += 1
            word += x[i]
            #drow = reversed(word)
            print (word, drow)