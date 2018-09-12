import lib

def main():
    text = input('Введите текст \n')

    if lib.is_palindrome(text):
        print('Этот текст является палиндромом')
    else:
        print('Этот текст не палиндром')


if __name__ == '__main__':
    main()