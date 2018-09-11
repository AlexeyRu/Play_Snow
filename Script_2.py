import lib

def main():
    text = input('Введите текст (только буквы латинского алфавита и цифры)\n')

    print('\nКоличество “отверстий” в тексте :', lib.sum_text_hole(text), 'штук')

if __name__ == '__main__':
    main()