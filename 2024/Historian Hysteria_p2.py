from collections import Counter


def read_input():
    left_list = []
    right_list = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if line:
                left, right = line.strip().split()
                left_list.append(int(left))
                right_list.append(int(right))
    return left_list, right_list


def caller():
    left, right = read_input()
    counter = Counter(num for num in right)
    left_set = set(left)
    total_sum = 0
    for left_num in left_set:
        count = counter.get(left_num, 0)
        total_sum += (left_num * count)
    return total_sum


if __name__ == "__main__":
    total = caller()
    print(total)
