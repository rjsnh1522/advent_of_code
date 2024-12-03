import re


def do_multiplication(mul_list):
    total = 0
    for i in mul_list:
        first, second = i
        total += (int(first) * int(second))
    return total


def find_all_matches(line):
    pattern = r"mul\((\d+),\s*(\d+)\)"
    matches = re.findall(pattern, line)
    return matches


def part_1(line):
    return find_all_matches(line)


def part_2(line):
    char_list = []
    skipping = False
    index = 0
    while index < len(line):
        if line[index] == 'd':
            if index + 6 < len(line) and line[index:index+7] == "don't()":
                skipping = True
                index += 7
                continue
            elif index + 3 < len(line) and line[index:index+4] == 'do()':
                skipping = False
                index += 4
                continue

        if not skipping:
            char_list.append(line[index])

        index += 1
    all_match = find_all_matches(''.join(char_list))
    return all_match


def read_input():
    part_1_all_matches = []
    part_2_str = []
    with open('input.txt') as file:
        line = file.read().strip()
        part_1_list = part_1(line)
        part_1_all_matches.extend(part_1_list)
        part_2_list = part_2(line)
        part_2_str.extend(part_2_list)
    final_sum = do_multiplication(part_1_all_matches)
    part_2_sum = do_multiplication(part_2_str)
    return final_sum, part_2_sum


if __name__ == "__main__":
    final_sum, part_2_sum = read_input()
    print(final_sum)
    print(part_2_sum)
