#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elem in my_list:
        if elem == search:
            new_list.append(relace)
        else:
            new_list.append(elem)
        return new_list
    my_list = [1, 2, 3, 4, 5, 3, 2, 1]
    searched_replaced_list = search_replace(my_list, 3, 0)
    print(searched_replaced_list)
