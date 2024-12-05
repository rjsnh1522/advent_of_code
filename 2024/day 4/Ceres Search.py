def find_xmas_in_all_direction(matrix, i, j, rows, cols):
    total_xmas_found = 0
    # Helper function to check if indices are valid
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    try:
        # toward right
        if is_valid(i, j + 3):
            char = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i][j + 3]
            if char == "XMAS":
                total_xmas_found += 1

        # towards left
        if is_valid(i, j - 3):
            char = matrix[i][j] + matrix[i][j - 1] + matrix[i][j - 2] + matrix[i][j - 3]
            if char == "XMAS":
                total_xmas_found += 1

        # bottom
        if is_valid(i + 3, j):
            char = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j]
            if char == "XMAS":
                total_xmas_found += 1

        # up
        if is_valid(i - 3, j):
            char = matrix[i][j] + matrix[i - 1][j] + matrix[i - 2][j] + matrix[i - 3][j]
            if char == "XMAS":
                total_xmas_found += 1

        # bottom right
        if is_valid(i + 3, j + 3):
            char = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3]
            if char == "XMAS":
                total_xmas_found += 1

        # up left
        if is_valid(i - 3, j - 3):
            char = matrix[i][j] + matrix[i - 1][j - 1] + matrix[i - 2][j - 2] + matrix[i - 3][j - 3]
            if char == "XMAS":
                total_xmas_found += 1

        # bottom left
        if is_valid(i + 3, j - 3):
            char = matrix[i][j] + matrix[i + 1][j - 1] + matrix[i + 2][j - 2] + matrix[i + 3][j - 3]
            if char == "XMAS":
                total_xmas_found += 1

        # up right
        if is_valid(i - 3, j + 3):
            char = matrix[i][j] + matrix[i - 1][j + 1] + matrix[i - 2][j + 2] + matrix[i - 3][j + 3]
            if char == "XMAS":
                total_xmas_found += 1

    except Exception as e:
        print(f"Error at position ({i}, {j}): {e}")

    return total_xmas_found





def part_1(matrix):
    total_xmas_found = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "X":
                total_xmas_found += find_xmas_in_all_direction(matrix=matrix, i=i, j=j, rows=rows, cols=cols)
    return total_xmas_found


def find_x_mas_in_all_direction(matrix, i, j, rows, cols):
    total_x_mas_found = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    if is_valid(i, j) and is_valid(i - 1, j - 1) and is_valid(i - 1, j + 1) and is_valid(i + 1, j - 1) and is_valid(
            i + 1, j + 1):
        # Pattern 1: Both diagonals MAS
        if (matrix[i][j] == "A" and
                matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S" and
                matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S"):
            total_x_mas_found += 1

        # Pattern 2: Both diagonals SAM
        if (matrix[i][j] == "A" and
                matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M" and
                matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M"):
            total_x_mas_found += 1

        # Pattern 3: First diagonal MAS, second diagonal SAM
        if (matrix[i][j] == "A" and
                matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S" and
                matrix[i - 1][j + 1] == "S" and matrix[i + 1][j - 1] == "M"):
            total_x_mas_found += 1

        # Pattern 4: First diagonal SAM, second diagonal MAS
        if (matrix[i][j] == "A" and
                matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M" and
                matrix[i - 1][j + 1] == "M" and matrix[i + 1][j - 1] == "S"):
            total_x_mas_found += 1

    return total_x_mas_found


def alternate(matrix, i, j, rows, cols):
    total_x_mas_found = 0
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    # Check all positions are valid first
    if not (is_valid(i, j) and is_valid(i - 1, j - 1) and is_valid(i - 1, j + 1)
            and is_valid(i + 1, j - 1) and is_valid(i + 1, j + 1)):
        return 0

    # Check first diagonal (top-left to bottom-right)
    tl_br_forward = (matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1]) == "MAS"
    tl_br_backward = (matrix[i + 1][j + 1] + matrix[i][j] + matrix[i - 1][j - 1]) == "MAS"
    first_diagonal_valid = tl_br_forward or tl_br_backward

    # Check second diagonal (top-right to bottom-left)
    tr_bl_forward = (matrix[i - 1][j + 1] + matrix[i][j] + matrix[i + 1][j - 1]) == "MAS"
    tr_bl_backward = (matrix[i + 1][j - 1] + matrix[i][j] + matrix[i - 1][j + 1]) == "MAS"
    second_diagonal_valid = tr_bl_forward or tr_bl_backward

    # If both diagonals form MAS (in either direction), we found an X-MAS
    if first_diagonal_valid and second_diagonal_valid:
        total_x_mas_found += 1

    return total_x_mas_found


def part_2(matrix):
    total_x_mas_found = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "A":
                total_x_mas_found += find_x_mas_in_all_direction(matrix=matrix, i=i, j=j, rows=rows, cols=cols)
    return total_x_mas_found


def read_input():
    matrix = []
    with open('input.txt') as file:
        for line in file:
            chars = list(line.strip())
            if chars:
                matrix.append(chars)
    return part_1(matrix), part_2(matrix)


if __name__ == "__main__":
    p_1_count, p_2_count = read_input()
    print(p_1_count, p_2_count)