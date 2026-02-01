def BinaryPascalTriangle():
    binary_str = input("Enter your bool function: ")

    row = [int(bit) for bit in binary_str]
    rows = len(row)

    triangle = [row]

    for i in range(rows - 1):
        new_row = []
        for j in range(len(triangle[i]) - 1):
            new_row.append(triangle[i][j] ^ triangle[i][j + 1])
        triangle.append(new_row)

    max_width = len(' '.join(map(str, triangle[0])))
    
    for i in range(len(triangle)):
        current_row = ' '.join(map(str, triangle[i]))
        spaces = (max_width - len(current_row)) // 2
        print(' ' * spaces + current_row)

BinaryPascalTriangle()