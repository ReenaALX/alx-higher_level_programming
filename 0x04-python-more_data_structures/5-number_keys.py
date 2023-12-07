#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for key in a_dictionary:
        count += 1
    return count

my_dict = {'apple': 2, 'banana': 3, 'cherry': 5}
num_of_keys = number_keys(my_dict)
print(num_of_keys)
