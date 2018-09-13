import lib

def main():

    assert lib.most_frequent_characters("12233344445555566666777777788888888999999999")=='9'
    assert lib.most_frequent_characters("q`112436456879809-0=-@#$%^&*()?=]p\|\/.,\\\\\\\\\\\\\\\whkhv l'n  jlnll")=='\\'

    print(lib.most_frequent_characters("q`112436456879809-0=-=]p\|\/.,\\\\\\\\\\\\\\\\\whkhv l'n  jlnl   l"))


if __name__ == '__main__':
    main()