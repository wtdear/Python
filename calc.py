# calculator
import math
from math import *

def calc ():
    arg = input("Введите действие: ")

    if arg == "//":
        number = int(input("Введите число: "))
        if number <= 0:
            print('Вы ввели некорректное значение\n'), calc()

        else:
            print("Квадратный корень из ", number, " равен: ", sqrt(numbers), "\n"), calc()

    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if arg == "+":
        print("Сумма: ", num1 + num2, "\n"), calc()

    elif arg == "-":
        print("Разность: ", num1 - num2, "\n"), calc()

    elif arg == "*":
        print('Произведение: ', num1 * num2, "\n"), calc()
    
    elif arg == "/":
        if num2 == 0:
            print('На ноль делить нельзя\n'), calc()
        
        else:
            print("Частное: ", num1 / num2, "\n"), calc()

    elif arg == "**":
        print("Число ", num1, " в степени ", num2, " равно: ", num1 ** num2, "\n"), calc()
    
    else:
        print("Возможно вы ошиблись действием, вот перечень:\nСумма (+)\nРазница (-)\nДеление - (/)\nУмножение - (*)\nВозведение в степень - (**)\nИзвлечение корня - (//)\n"), calc()

calc()