import random
from random import *

# === List ===
simvols = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'A', 'B', 'C', 'D', 'E', 'F', 'G',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] #24 simv

# === Main ===
def generate():
    change = int(input('Вы желаете сгенерировать пароль с определённой длиной или нет?\n1 - да\n2 - нет\nЯ выбираю: '))
    
    if change == 1:
        dlina = int(input('Укажите длину списка ( от 4 до 24 ): '))
        if dlina < 4 or dlina > 24:
            print('Вы ввели некорректное значение\n'), generate()
        else:
            password = ''.join(sample(simvols, dlina))
            print(f'Ваш сгенерированный пароль: {password}\nДлина вашего пароля: {len(password)}\n'), generate()

    elif change == 2:
        print('\nВаш сгенерированный пароль ( 24 символа ):')
        print(''.join(sample(simvols, len(simvols))))
        print(), generate()

    else:
        print('Вы выбрали неверное значение, попробуйте ещё раз\n'), generate()

generate()