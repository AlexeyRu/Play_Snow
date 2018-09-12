import lib

def main():
    print('Введите исход игры в "крестики нолики" по строкам. В конце каждой строки жмем "Enter:\n')
    x = []
    while len(x) < 3:
        y = lib.check_input_TicTacToe_state(input())
        if y[0] == False:
            print(y[1])
        else:
            x.append(y)


    print('Было введено:\n', x)


    print('Выиграл игрок ', lib.find_winner(x))
if __name__ == '__main__':
    main()