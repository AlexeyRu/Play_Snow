import lib

def main():
    x=[]
    y = input('Введите исход иигры в "крестики нолики" по строкам. В конце каждой строки жмем "Enter":\n')
    x.append(y)
    x.append(input())
    x.append(input())

    print('Было введено:\n', x)


    print('Выиграл игрок ', lib.find_winner(x))
if __name__ == '__main__':
    main()