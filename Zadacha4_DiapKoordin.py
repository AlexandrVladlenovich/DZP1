planeNum = int(input('Введите номер четверти оси координат: '))
if planeNum == 1:
    print('(Х > 0; Y > 0)')
elif planeNum == 2:
    print('(Х < 0; Y > 0)')
elif planeNum == 3:
    print('(Х < 0; Y < 0)')
elif planeNum == 4:
    print('(Х > 0; Y < 0)')
else:
    print('Пожалуйста, введите корректное значение номера плоскости')