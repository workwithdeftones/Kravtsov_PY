#Даны три переменные вещественного типа: A, B, C. Если их значения упорядочены по возрастанию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное. Вывести новые значения переменных A, B, C
a = float(input("Введите значение A: "))
b = float(input("Введите значение B: "))
c = float(input("Введите значение C: "))

if a <= b <= c:  # Проверка на возрастание
    a *= 2
    b *= 2
    c *= 2
else:  # В противном случае
    a = -a
    b = -b
    c = -c

print("Новые значения:")
print("A =", a)
print("B =", b)
print("C =", c)