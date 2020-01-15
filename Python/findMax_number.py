# Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based
# on the following rules.
# 1. Always num1 should be less than num2
# 2. Consider each number from num1 to num2 (num2 inclusive).
#       Populate the number into a list, if the below conditions are satisfied
#           a. Sum of the digits of the number is a multiple of 3
#           b. Number has only two digits
#           c. Number is a multiple of 5
# 3. Display the maximum element from the list
# In case of any invalid data or if the list is empty, display -1.


def find_max(num1, num2):
    max_num = -1
    # Write your logic here
    # Check num2 should be greated that num1
    if(num1 > num2):
        return max_num
    else:
        # Check length of number
        if(len(str(num1)) == 2 and len(str(num2)) == 2):  # Number has only two digits
            for number in range(num1, num2+1):
                first = str(number)[0]
                second = str(number)[1]
                result = int(first) + int(second)
                if(result % 3 == 0):  # Sum of digits of the number should be multiple of 3
                    # print(f"Number: {number} is a multiple of 3")
                    if(number % 5 == 0):
                        if(number > max_num):
                            max_num = number
        else:
            max_num = -1  # Invalid entry
    return max_num


# Provide different value s for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)
