# Пирамидка из звездочек будет

def main ():

    type = int(input("Вы хотите построить лестницу (1) или пирамидку (2) ?: "))

    if type == 1:
        levels = int(input("Введите количество ступенек: "))
        for i in range(1, levels + 1):
            print("*" * i)

    elif type == 2:
        levels = int(input("Введите количество уровней пирамидки: "))
        for i in range(0, levels):
            print(" " * (levels - i) + "*" * (2 * i + 1))

    else:
        print("Вы ввели некорректный символ, попробуйте ещё раз <3\n"), main()

main()