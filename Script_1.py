import lib

def main():
    text = input('Введите текст (только буквы латинского алфавита и цифры)\n')

    print('\nСамые часто встречающиеся символы :', lib.most_frequent_characters(text))


if __name__ == '__main__':
    main()