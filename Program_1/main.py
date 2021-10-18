from typing import TextIO


def program1(file: TextIO):
    contents = file.read()
    numbers = [int(s) for s in contents.split('\n')]
    answer = sum(numbers)
    file.write('\n' + str(answer))
