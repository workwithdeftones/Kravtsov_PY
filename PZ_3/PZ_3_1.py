#Дано целое положительное число. Проверить истинность высказывания: «Данное число является четным двузначным».
number = int(input("Введите двузначное число: "))

if number < 10 or number > 100:
    print("Число не двузначное")
elif number % 2 == 0:
    print("Данное число является четным двузначным")
elif number % 2 == 1:
    print("Данное число является нечетным двузначным")