import lib

def main():

    assert lib.is_palindrome("А роза упала на лапу Азора") == True
    assert lib.is_palindrome("А роза упала на лапу Азора ") == True
    assert lib.is_palindrome("А роза не упала на лапу Азора ") == False
    assert lib.is_palindrome("Sum\ summus \mus") == True

    print(lib.is_palindrome("Sum summus mus"))


if __name__ == '__main__':
    main()