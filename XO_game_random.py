from random import choice


def xo_easy():
    def draw_legend():
        board = list(range(1, 10))
        print("-" * 13)
        for i in range(3):
            print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
            print("-" * 13)

    def draw_board():
        print("-" * 13)
        for row in board_array:
            print('|', end='')
            for cell in row:
                if cell == 0:
                    print(' ' * 3 + '|', end='')
                elif cell == 1:
                    print(' ' + 'X' + ' |', end='')
                elif cell == 10:
                    print(' ' + 'O' + ' |', end='')
            print()
            print("-" * 13)

    def victory_conditions():
        for row in board_array:
            if sum(row) == 3:
                return 1
            elif sum(row) == 30:
                return 2
        for i in range(3):
            if board_array[0][i] + board_array[1][i] + board_array[2][i] == 3:
                return 1
            elif board_array[0][i] + board_array[1][i] + board_array[2][i] == 30:
                return 2
        if board_array[0][0] + board_array[1][1] + board_array[2][2] == 3:
            return 1
        elif board_array[0][0] + board_array[1][1] + board_array[2][2] == 30:
            return 2
        elif board_array[0][2] + board_array[1][1] + board_array[2][0] == 3:
            return 1
        elif board_array[0][2] + board_array[1][1] + board_array[2][0] == 30:
            return 10
        else:
            return 0

    def player_input_x(cell_var):
        if 0 <= cell_var <= 3:
            if board_array[0][cell_var - 1] == 0:
                board_array[0][cell_var - 1] = 1
                check_board.remove(cell_var)

        elif 4 <= cell_var <= 6:
            if board_array[1][cell_var - 4] == 0:
                board_array[1][cell_var - 4] = 1
                check_board.remove(cell_var)

        elif 7 <= cell_var <= 9:
            if board_array[2][cell_var - 7] == 0:
                board_array[2][cell_var - 7] = 1
                check_board.remove(cell_var)

        return board_array

    def player_input_o(cell_var):
        if 0 <= cell_var <= 3:
            if board_array[0][cell_var - 1] == 0:
                board_array[0][cell_var - 1] = 10
                check_board.remove(cell_var)

        elif 4 <= cell_var <= 6:
            if board_array[1][cell_var - 4] == 0:
                board_array[1][cell_var - 4] = 10
                check_board.remove(cell_var)

        elif 7 <= cell_var <= 9:
            if board_array[2][cell_var - 7] == 0:
                board_array[2][cell_var - 7] = 10
                check_board.remove(cell_var)

        return board_array

    def cpu_input_o():
        cell_var = choice(check_board)
        if 0 <= cell_var <= 3:
            board_array[0][cell_var - 1] = 10
            check_board.remove(cell_var)
        elif 4 <= cell_var <= 6:
            board_array[1][cell_var - 4] = 10
            check_board.remove(cell_var)
        elif 7 <= cell_var <= 9:
            board_array[2][cell_var - 7] = 10
            check_board.remove(cell_var)

        return board_array

    def cpu_input_x():
        cell_var = choice(check_board)
        if 0 <= cell_var <= 3:
            board_array[0][cell_var - 1] = 1
            check_board.remove(cell_var)
        elif 4 <= cell_var <= 6:
            board_array[1][cell_var - 4] = 1
            check_board.remove(cell_var)
        elif 7 <= cell_var <= 9:
            board_array[2][cell_var - 7] = 1
            check_board.remove(cell_var)

        return board_array


    check_board = list(range(1, 10))
    board_array = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    while True:
        side_player = input('Если хотите играть за Х, введите x\n'
                            'Если хотите играть за О, введите o')
        side_player = side_player.lower()
        if side_player == 'x' or side_player == 'o':
            break
        elif side_player != 'x' or side_player != 'o':
            print('Неверный ввод, повторите выбор')

    draw_legend()
    if side_player == 'x':
        while True:
            cell_var = int(input('Игрок, введите адрес поля от 1 до 9'))
            while True:
                if cell_var in check_board:
                    break
                else:
                    print('Эта ячейка занята или не существует, повторите ввод')
                    cell_var = int(input('Игрок, введите адрес поля от 1 до 9'))

            board_array = player_input_x(cell_var)
            win_check = victory_conditions()
            if len(check_board) == 0 and win_check == 0:
                draw_board()
                print('Ничья')
                break
            board_array = cpu_input_o()
            win_check = victory_conditions()
            if len(check_board) == 0 and win_check == 0:
                draw_board()
                print('Ничья')
                break
            draw_legend()
            draw_board()
            win_check = victory_conditions()
            if win_check == 1:
                print('Выиграл Х')
                break
            elif win_check == 2:
                print('Выиграл О')
                break
            continue

    elif side_player == 'o':
        while True:
            board_array = cpu_input_x()
            win_check = victory_conditions()
            if len(check_board) == 0 and win_check == 0:
                draw_board()
                print('Ничья')
                break

            draw_board()
            win_check = victory_conditions()
            if win_check == 1:
                print('Выиграл Х')
                break
            elif win_check == 2:
                print('Выиграл О')
                break
            cell_var = int(input('Игрок, введите адрес поля от 1 до 9'))
            while True:
                if cell_var in check_board:
                    break
                else:
                    print('Эта ячейка занята или не существует, повторите ввод')
                    cell_var = int(input('Игрок, введите адрес поля от 1 до 9'))

            board_array = player_input_o(cell_var)
            win_check = victory_conditions()
            if len(check_board) == 0 and win_check == 0:
                draw_board()
                print('Ничья')
                break
            continue

    dict_win = {'Wins': 0, 'Dead heat': 0, 'Lose': 0, 'Games': 0}
    if side_player == 'o' and win_check == 2:
        dict_win['Wins'] = 1
    elif side_player == 'x' and win_check == 1:
        dict_win['Wins'] = 1
    elif win_check == 0:
        dict_win['Dead heat'] = 1
    else:
        dict_win['Lose'] = 1

    dict_win['Games'] = 1

    return dict_win
