import math

def square(side):
    # Вычисляем площадь
    area = side * side
    # Округляем результат вверх
    return math.ceil(area)

print(square(3.5))
print(square(4))