import lib


def main():
    """
    main function
    :return:
    """
    '''
    print('Введите исход игры в "крестики нолики" по строкам. В конце каждой строки жмем "Enter:\n')
    x = []
    while len(x) < 3:
        y = lib.check_input_tictactoe_state(input())
        if y[0] == False:
            print(y[1])
        else:
            x.append(y)

    print('Было введено:\n', x)
    print('Выиграл игрок ', lib.find_winner(x))
    '''

    assert lib.find_winner(['XOX',
                            'OXO',
                            'XOO']) == 'X'

    assert lib.find_winner(['XOX',
                            'OXO',
                            'OOX']) == 'X'

    assert lib.find_winner(['OXO',
                            'XOX',
                            'XXO']) == 'O'

    assert lib.find_winner(['OXO',
                            'XOO',
                            'OOX']) == 'O'

    assert lib.find_winner(['OOO',
                            'OXO',
                            'XOX']) == 'O'

    assert lib.find_winner(['OXO',
                            'OXO',
                            'OOX']) == 'O'

    assert lib.find_winner(['XXX',
                            'OXO',
                            'OOX']) == 'X'

    assert lib.find_winner(['OXO',
                            'XXO',
                            'OXX']) == 'X'

    assert lib.find_winner(['OXO',
                            'XXO',
                            'OOX']) == 'D'

    assert lib.find_winner(['OOX',
                            'XXO',
                            'OXX']) == 'D'


if __name__ == '__main__':
    main()