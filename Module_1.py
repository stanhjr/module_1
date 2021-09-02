import json
from sortings import bublle_sort, quick_sort, merge_sort, sort_two_list
from filter_dictionary import unique_keys
from brick_wall import brick_wall
from XO_game_random import xo_easy
from xo_game_hard import xo_hard


def string_to_list(string_user: str):
    string_user = string_user.split()
    string_user = list(map(int, string_user))
    return string_user


def menu():
    print('Какое дейсвтие вам интересно в данный момент?')
    print('1 - отсортировать список чисел методом "пузырька"')
    print('2 - отсортировать список чисел методом "быстрой сортировки"')
    print('3 - отсортировать список чисел методом "слияния"')
    print('4 - напечатать результат расчёта кирпичной стены')
    print('5 - напечатать список из словарей, где набор значений по ключам из второго списка является уникальным')
    print('6 - Игра "Крестики - нолики", сложность - Easy')
    print('7 - Игра "Крестики - нолики", сложность - Hard')
    print('8 - если вы хотите внести изменения в ваш профайл')
    print('q - если вы хотите завершить выполнение программы')


try:
    f = open('profile.txt')
    print('Здравствуйте, ', f.read())
    f.close()

except IOError:
    print('Здравствуйте, мы пока не знакомы, представьтесь пожалуйста')
    name = input('Введите ваше имя')
    name = name.lower()
    name = name.capitalize()
    f = open('profile.txt', 'w')
    f.write(name)
    print('Спасибо, ', name)
    f.close()

while True:
    menu()
    user_input = input()
    if user_input == '1':
        string_list = input('Введите массив чисел через пробел')
        string_list = string_to_list(string_list)
        string_list = bublle_sort(string_list)
        print(string_list)
        continue

    elif user_input == '2':
        string_list = input('Введите массив чисел через пробел')
        string_list = string_to_list(string_list)
        string_list = quick_sort(string_list)
        print(string_list)
        continue

    elif user_input == '3':
        string_list = input('Введите массив чисел через пробел')
        string_list = string_to_list(string_list)
        string_list = merge_sort(string_list)
        print(string_list)
        continue

    elif user_input == '4':
        brick_wall()

    elif user_input == '5':
        list_dict = input('Введите список словарей')
        list_dict = list_dict.replace("'", '"')
        list_dict = json.loads(list_dict)
        print('Вот ваш список словарей')
        print()
        for i in list_dict:
            print(i)
        list_key = input('Введите список строк с ключами из словаря')
        list_key = list_key.split()
        unique_keys = unique_keys(list_dict, list_key)
        print('А вот и результат')
        print()
        for i in unique_keys:
            print(i)
        print()

    elif user_input == '6':
        f = open('result.txt', 'r')
        count = json.loads(f.read())
        f.close()
        for i in count:
            print(i, ' - ', count[i])
        result = xo_easy()
        for key in result:
            result[key] += count[key]
        result = json.dumps(result)
        with open('result.txt', 'w') as f:
            f.write(result)
            f.close()

    elif user_input == '7':
        with open('result.txt', 'r') as f:
            count = json.loads(f.read())
            f.close()
        for i in count:
            print(i, ' - ', count[i])
        result = xo_hard()
        for key in result:
            result[key] += count[key]
        result = json.dumps(result)
        with open('result.txt', 'w') as f:
            f.write(result)
            f.close()

    elif user_input == '8':
        name = input('Введите новое имя')
        name = name.lower()
        name = name.capitalize()
        f = open('profile.txt', 'w')
        f.write(name)
        print('Спасибо, ', name)
        f.close()
        continue

    elif user_input == 'q':
        print('Завершаю выполнение программы, до скорых встреч')
        break

    else:
        print('Неправильный ввод, повторите попытку')
