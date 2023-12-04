replace_dict = {'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'}


def prefix(string):
    for key, value in replace_dict.items():
        if string.startswith(key):
            return value
    if string[0].isnumeric():
        return string[0]
    return prefix(string[1:])


def suffix(string):
    for key, value in replace_dict.items():
        if string.endswith(key):
            return value
    if string[-1].isnumeric():
        return string[-1]
    return suffix(string[:-1])


input = open('input.txt')
lines = input.readlines()
input.close()

sum = 0
for line in lines:
    number = prefix(line) + suffix(line)
    sum += int(number)

print(sum)
