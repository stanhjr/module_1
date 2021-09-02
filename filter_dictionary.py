
def unique_keys(list_dict: list, list_key: list):
    """returns a list of dictionaries with unique keys from a list of keys"""

    list_of_unique_dictionaries = []
    filter_list = []

    for dictionary in list_dict:
        list_trash = []
        for elem in list_key:
            list_trash.append(dictionary[elem])
        if list_trash not in filter_list:
            filter_list.append(list_trash)
            list_of_unique_dictionaries.append(dictionary)
    return list_of_unique_dictionaries
