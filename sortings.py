

def sort_two_list(list_left, list_right):
    sorted_list = []
    left_lenght = len(list_left)
    right_lenght = len(list_right)
    idx_left = 0
    idx_right = 0

    while idx_left < left_lenght and idx_right < right_lenght:
        if list_left[idx_left] <= list_right[idx_right] and idx_left < left_lenght:
            sorted_list.append(list_left[idx_left])
            idx_left += 1
        elif list_left[idx_left] > list_right[idx_right] and idx_right < right_lenght:
            sorted_list.append(list_right[idx_right])
            idx_right += 1

    while idx_left < left_lenght:
        sorted_list.append(list_left[idx_left])
        idx_left += 1

    while idx_right < right_lenght:
        sorted_list.append(list_right[idx_right])
        idx_right += 1
    return sorted_list


def merge_sort(unsorted_list: list):
    if len(unsorted_list) == 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[:middle])
    right = merge_sort(unsorted_list[middle:])
    return sort_two_list(left, right)


def bublle_sort(consistently):
    """bubble sorts"""

    for j in range(len(consistently) - 1):
        for i in range(len(consistently) - j - 1):
            if consistently[i] > consistently[i + 1]:
                consistently[i], consistently[i + 1] = consistently[i + 1], consistently[i]
    return consistently


def quick_sort(list_sorting):
    if len(list_sorting) <= 1:
        return list_sorting

    base_elem = list_sorting[0]
    left = list(i for i in list_sorting if i < base_elem)
    center = list(i for i in list_sorting if i == base_elem)
    right = list(i for i in list_sorting if i > base_elem)

    return quick_sort(left) + center + quick_sort(right)
