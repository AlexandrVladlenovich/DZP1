dotA_X = int(input('Введите координаты точки А по оси х: '))
dotA_Y = int(input('Введите координаты точки А по оси y: '))
dotB_X = int(input('Введите координаты точки B по оси х: '))
dotB_Y = int(input('Введите координаты точки B по оси y: '))

distance = (((dotB_X - dotA_X) ** 2) + ((dotB_Y - dotA_Y) ** 2)) ** 0.5
print(distance)