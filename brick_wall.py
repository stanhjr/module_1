import sys
import copy

def brick_wall():


    # Creating functions
    def most_common(lst):
        """returns the most frequently occurring value"""
        flat_list = [el for sublist in lst for el in sublist]
        return max(flat_list, key=flat_list.count)


    def search_most_common(number, array_2D):
        """returns the number of occurrences of a number in a 2D array"""
        result = 0
        for r in array_2D:
            for b in r:
                if b == number:
                    result += 1
        return result


    def walls_list_remove(brick_length, wall):
        """removes matching elements"""
        for row in wall:
            for b in row:
                if b == brick_length:
                    row.remove(b)


    def draw_empty_wall(w):
        """draw an empty wall"""
        print('+' + '-' * (sum(row) + len(wall[0]) - 1) + '+')
        for r in w:
            print('|', end='')
            for b in r:
                print(' ' * b + '|', end='')
            print()
        print('+' + '-' * (sum(row) + len(wall[0]) - 1) + '+')


    def most_common_upd(lst):
        """returns the most frequently occurring value"""
        flat_list = [el for sublist in lst for el in sublist]
        max_search_list = []
        y = max(flat_list, key=flat_list.count)
        z = flat_list.count(y)
        for i in flat_list:
            if flat_list.count(i) == z:
                max_search_list.append(i)
        max_search_list = set(max_search_list)
        max_search_list = list(max_search_list)
        max_search_list.sort()
        return max_search_list


    print('Уважаемый пользователь, вы должны ввести несколько строк содержащих цифры от 1 включительно через пробел\n'
          'для введения следующего ряда нажмите клавишу Enter, когда вы решите, что ввод завершён \n'
          'введите go b нажмите Enter ')


    row_wall_input = input()
    wall = []

    while row_wall_input != 'go':
        row_input = list(map(int, row_wall_input.split()))
        wall.append(row_input)
        row_wall_input = input()

    first_row_wall = sum(wall[0])

    # check validation
    for row in wall:
        if sum(row) == 0:
            print('Ряд равен нулю, не надо так делать. '
                  '\nЗавершаю выполнение программы!')
            sys.exit()

    # calculate the number of all elements of a two-dimensional array
    num_all_elem = 0
    for i in wall:
        num_all_elem += len(i)

    # exceptions for series of the same element
    res = 0
    for row in wall:
        for b in row:
            if b == wall[0][0]:
                res += 1

    if res == num_all_elem:
        print('В любом положении линии она пересечет одинаковое количество кирпичей\n'
              'Пусть ответ будет единица, но настоящие строители так не строят :)')
        draw_empty_wall(wall)
        sys.exit()

    for row in wall:
        if sum(row) != first_row_wall:
            print('С такими параметрами стена не будет прямоугольной, \nно я сейчас подправлю стену за вас')
            print()
            break

    # finding the longest row on the wall
    l_row = 0
    for row in wall:
        if sum(row) > l_row:
            l_row = sum(row)

    # matrix creation
    for row in wall:
        if sum(row) < l_row:
            row.append(l_row - sum(row))

    # finding the max length row on the wall
    max_length_row = 0
    for row in wall:
        if len(row) > max_length_row:
            max_length_row = len(row)

    # creating a list of sums of items
    walls_list = copy.deepcopy(wall)
    for row in range(len(walls_list)):
        for b in range(1, len(walls_list[row])):
            walls_list[row][b] += walls_list[row][b - 1]

    # minimum crossing equals most frequent item
    minimal_crossing = most_common(walls_list)

    # eliminating intersections on finished blocks
    for i in range(l_row):
        if search_most_common(minimal_crossing, walls_list) == len(wall):
            walls_list_remove(minimal_crossing, walls_list)
            minimal_crossing = most_common(walls_list)

    array_matches = most_common_upd(walls_list)

    for elem in array_matches:
        print('Положение линии, в котором она пересекает наименьшее количество кирпичей = ', elem)

    # draw a wall
    print('+' + '-' * (array_matches[0] - 1) + 'x', end='')
    for i in range(1, len(array_matches)):
        print('-' * (array_matches[i] - array_matches[i - 1] - 1) + 'x', end='')
    print('-' * (sum(wall[0]) - array_matches[-1] - 1) + '+', end='')
    print()

    for row in wall:
        print('|', end='')
        ind = 0
        rep_x = 0
        for b in row:
            counter = 0
            kep = 0
            for i in range(len(array_matches)):
                container = ""
                compensator = 0
                if sum(row[:ind + 1]) > array_matches[i] > sum(row[:ind]):
                    counter += 1
                    if counter > 1:
                        continue
                    for idx in range(len(array_matches)):
                        if sum(row[:ind + 1]) > array_matches[idx] > sum(row[:ind]):
                            zep_x = (array_matches[idx] - sum(row[:ind]) - compensator)
                            container += ' ' * (zep_x - 1) + 'x'
                            compensator += zep_x
                            z = b
                    print(container + ' ' * (b - compensator - 1) + '|', end='')
                    ind += 1
                    kep += 1

            if ind > len(row) - 1:
                continue
            if kep == 0:
                print(' ' * (b - compensator - 1) + '|', end='')
                ind += 1

        print()
        ind = 0

    print('+' + '-' * (array_matches[0] - 1) + 'x', end='')
    for i in range(1, len(array_matches)):
        print('-' * (array_matches[i] - array_matches[i - 1] - 1) + 'x', end='')
    print('-' * (sum(wall[0]) - array_matches[-1] - 1) + '+', end='')
    print()
