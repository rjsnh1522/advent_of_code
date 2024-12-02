
def check_strictly_decreasing(elements):
    prev = elements[0]
    for num in elements[1:]:
        if not int(prev) > int(num):
            return False
        prev = num
    return True

def check_strictly_increasing(elements):
    prev = elements[0]
    for num in elements[1:]:
        if not int(prev) < int(num):
            return False
        prev = num
    return True


def check_diff(elements):
    prev = elements[0]
    for num in elements[1:]:
        if abs(int(prev) - int(num)) not in [1,2,3]:
            return False
        prev = num
    return True


def strictly_increasing_or_decreasing(line):
    elements = line.split()
    is_strictly_decreasing, correct_diff = False, False
    elements = [i for i in map(int, elements)]
    for j in range(len(elements)):
        els = elements[:j] + elements[j+1:]
        is_strictly_inc_or_dec = check_strictly_increasing(els)
        if not is_strictly_inc_or_dec:
            is_strictly_inc_or_dec = check_strictly_decreasing(els)
        if is_strictly_inc_or_dec:
            correct_diff = check_diff(els)
            if correct_diff:
                return True
    return False


def read_input():
    counter = 0
    with open('input', 'r') as file:
        for line in file.readlines():
            if line:
                dec = strictly_increasing_or_decreasing(line.strip())
                if all([dec]):
                    counter +=1
    return counter


if __name__ == "__main__":
    safe_reports = read_input()
    print(safe_reports)
