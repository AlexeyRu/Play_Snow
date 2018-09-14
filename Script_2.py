import lib


def main():

    assert lib.sum_text_hole("1234567890") == 6
    assert lib.sum_text_hole("qopdbRB") == 8
    assert lib.sum_text_hole("@%&") == 5


if __name__ == '__main__':
    main()
    