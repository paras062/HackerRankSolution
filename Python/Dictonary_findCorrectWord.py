# Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
# The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

# The function should identify the degree of correctness as mentioned below:
# CORRECT, if it is an exact match
# ALMOST CORRECT, if no more than 2 letters are wrong
# WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

# and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
# Assume that the words contain only uppercase letters and the maximum word length is 10.


# Sample Input                                                                                                Expected Output

# {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}                 [2, 2, 1]

def find_correct(word_dict):
    # start writing your code here
    count, correct_words, almost_correct_words, wrong_words = 0, 0, 0, 0

    for key, value in word_dict.items():
        if len(key) != len(value):
            wrong_words += 1
        else:
            diff_list = set(list(key)).symmetric_difference(set(list(value)))
            count = len(diff_list)
            if count == 0:
                correct_words += 1
            elif count <= 2:
                almost_correct_words += 1
            elif count > 2:
                wrong_words += 1
    return correct_words, almost_correct_words, wrong_words


# word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
word_dict = {'MIND': 'MUND', 'ALWAYS': 'ALLISWELL',
             'VENDOR': 'VENDING', 'RADIO': 'RADICAL', 'CHECK': 'CHEK'}
result = find_correct(word_dict)
result = list(result)
print(result)
