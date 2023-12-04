replace_dict = {'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'}


def first_num(string):
    for key, value in replace_dict.items():
        if string.startswith(key):
            return value
    if string[0].isnumeric():
        return string[0]
    return first_num(string[1:])


def last_num(string):
    for key, value in replace_dict.items():
        if string.endswith(key):
            return value
    if string[-1].isnumeric():
        return string[-1]
    return last_num(string[:-1])


input = open('input.txt')
lines = input.readlines()
input.close()

sum = 0
for line in lines:
    number = first_num(line) + last_num(line)
    sum += int(number)

print(sum)
