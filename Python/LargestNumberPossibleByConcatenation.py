# Write a python function, create_largest_number(), which accepts a list of numbers and returns the
# largest number possible by concatenating the list of numbers.
# Note: Assume that all the numbers are two digit numbers.

# Sample Input                  Expected Output
# 23,34,55                          553423


def sortIntegerDigit(x):
    x = str(x)
    a = int(x[0])
    b = int(x[1])
    number = ""
    if(a > b):
        number = str(a) + "" + str(b)
    else:
        number = str(b) + "" + str(a)
    return int(number)


def create_largest_number(number_list):
    largest_number = ""
    new_sorted_list = []
    temp = 0
    for items in number_list:
        temp = sortIntegerDigit(items)
        new_sorted_list.append(temp)
    new_sorted_list = sorted(new_sorted_list, reverse=True)

    for items in new_sorted_list:
        largest_number += str(items)
    return int(largest_number)


number_list = [23, 45, 67]  # [87, 22, 15]
largest_number = create_largest_number(number_list)
print(largest_number)
