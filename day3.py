with open("day3input.txt", 'r') as f:
    _input = f.readlines()

import string
alphabet = list(string.ascii_letters)

res = 0

def get_letter_value(letter):
    return alphabet.index(letter) + 1


def find_common(str1, str2):
    for j in str1:
        for i in str2:
            if i == j:
                return i

with open("day3input.txt", 'r') as f:
    _input = f.readlines()
    for i in range(0, len(_input)):
        com_one = _input[i][:int(len(_input[i]) / 2)]
        com_two = _input[i][int(len(_input[i]) / 2):]

        # Compare the two string for a common char
        common = find_common(com_one, com_two)

        if get_letter_value(common) > 0:
            res += get_letter_value(common)
print(res)
