def read_input():
    left_heap = []
    right_heap = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if line:
                left, right = line.strip().split()
                left_heap.append(int(left))
                right_heap.append(int(right))
    return left_heap, right_heap


def caller():
    left, right = read_input()
    left.sort()
    right.sort()
    total_diff = 0
    for i in range(len(left)):
        total_diff += abs(left[i] - right[i])
    return total_diff


if __name__ == "__main__":
    total = caller()
    print(total)