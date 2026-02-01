def PascalTriangle():
    rows = int(input("Enter rows: "))
    
    for i in range(rows):
        print(' ' * (rows - i), end='')
        number = 1
        
        for j in range(i + 1):
            print(f'{number:3}', end='')
            number = number * (i - j) // (j + 1)
        print()

PascalTriangle()