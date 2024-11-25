
def find_first_and_last_digit(line):
    left, right = 0, len(line)-1
    f_d = None
    r_d = None
    while left < right:
        if f_d is not None and r_d is not None:
            break
        else:
            if f_d is None and line[left].isdigit():
                f_d = int(line[left])
            if r_d is None and line[right].isdigit():
                r_d = int(line[right])
            right -= 1
            left += 1
    print(f"Number at each line {f_d}{r_d}")
    if r_d is None:
        r_d = f_d
    return int(f"{f_d}{r_d}")


def find_sum():
    total = 0
    with open('input.txt', 'r') as file:
        for i in file.readlines():
            number = find_first_and_last_digit(i)
            total += number

    return total


print(find_sum())

