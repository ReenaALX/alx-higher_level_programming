#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elem(elem):
        return (elem if elem != search else replace)
    return list(map(s_r_elem, my_list))
