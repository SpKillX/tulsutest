print("Задание 3 Факториал числа\n")
def factorial(number):
    if number == 1:
        return (number)
    else:
        return (number*factorial(number-1))

number = 5
if number < 0:
    print("Введите неотрицательное число\n")
elif number == 0:
    print("Факториал числа 0 равен ", 1, "\n")
else:
    print(f"Факториал числа {number} равен {factorial(number)}\n")