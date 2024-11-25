
def find_first_and_last_digit(line):
    digits = []
    for i in line:
        if i.isdigit():
            digits.append(i)
    return int(f"{digits[0]}{digits[-1]}")


def find_sum():
    total = 0
    with open('input.txt', 'r') as file:
        for i in file.readlines():
            number = find_first_and_last_digit(i.strip())
            total += number

    return total


print(find_sum())

