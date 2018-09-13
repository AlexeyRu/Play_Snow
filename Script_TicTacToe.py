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


if __name__ == '__main__':
    main()