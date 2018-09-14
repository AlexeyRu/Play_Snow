import lib


def main():
    """
    main function
    :return:
    """

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

    assert lib.find_winner(['XOX',
                            'XOX',
                            'OXO']) == 'D'

    assert lib.check_input_tictactoe_state('XOX') == (True, 'XOX')
    assert lib.check_input_tictactoe_state('XXO') == (True, 'XXO')
    assert lib.check_input_tictactoe_state('OXX') == (True, 'OXX')
    assert lib.check_input_tictactoe_state('oox') == (True, 'OOX')
    assert lib.check_input_tictactoe_state('ooo') == (True, 'OOO')
    assert lib.check_input_tictactoe_state('xxx') == (True, 'XXX')
    assert lib.check_input_tictactoe_state('[jj') == \
           (False, 'You use no correct symbols (only "X" and "O"). Try one more time!')
    assert lib.check_input_tictactoe_state('oxxx') == \
           (False, 'input is too long (need 3 symbols). Try one more time!')
    assert lib.check_input_tictactoe_state('ox') == \
           (False, 'input is too short (need 3 symbols). Try one more time!')

    print('Enter "Tic Tac Toe" gamestate by rows. Press "Enter" at each row end:\n')
    x = []
    while len(x) < 3:
        y = lib.check_input_tictactoe_state(input())
        if y[0] == False:
            print(y[1])
        else:
            x.append(y[1])

    print('The gamestate were entered:\n', x[0], '\n', x[1], '\n', x[2])
    print('\n Result: ')
    if lib.find_winner(x) == 'D':
        print('Nobody wins')
    else:
        print('The ', lib.find_winner(x), ' player wins')


if __name__ == '__main__':
    main()
