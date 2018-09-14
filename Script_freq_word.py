import lib


def main():

    assert lib.most_frequent_word("aaa bbb ccc bbb xxx aaa aaa xxx bbb") == 'aaa'
    assert lib.most_frequent_word(" aAa bbb ccc bbb xxx aaa aaA xxx bBb") == 'aaa'

    print(lib.most_frequent_word(" aAa bbb ccc bbb xxx aaa aaA xxx bBb"))


if __name__ == '__main__':
    main()
