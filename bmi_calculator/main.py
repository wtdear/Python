weigt = int(input("Введите ваш вес - "))
height = int(input("Введите ваш рост - "))

def BMI(weigt, height):
    height_in_meters = height / 100
    bmi = weigt / (height_in_meters ** 2)
    return bmi
     
print(f"Ваш ИМТ: {BMI(weigt, height):.1f}")
input("Нажмите Enter для завершения программы")
