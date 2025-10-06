import matplotlib

print("ВАРИАНТ 11\n\n")


print("Задание 1 Таблица умножения\n")
for i in range(1, 11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("\n")


print("Задание 3 Факториал числа\n")
def factorial(number):
    if number == 1:
        return (number)
    else:
        return (number*factorial(number-1))

number = int(input("Введите число: "))
if number < 0:
    print("Введите неотрицательное число\n")
elif number == 0:
    print("Факториал числа 0 равен ", 1, "\n")
else:
    print(f"Факториал числа {number} равен {factorial(number)}\n")