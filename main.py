import matplotlib.pyplot

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

number = 5
if number < 0:
    print("Введите неотрицательное число\n")
elif number == 0:
    print("Факториал числа 0 равен ", 1, "\n")
else:
    print(f"Факториал числа {number} равен {factorial(number)}\n")


print("Задание 5 Список простых чисел до 100\n")
max_number = 100
for numbers in range(2, max_number+1):
    is_prime = True
    for i in range(2, int(numbers**0.5)+1):
        if numbers % i == 0:
            is_prime = False
            break
    if is_prime:
        print(numbers, end=" ")
print("\n\n")


print("Задание 1 (повышенная сложность) Сортировка списка пузырьком\n")
numbers_to_sort = [15, 35, 78, 1, 2, 64, 34, 25, 12, 22, 11, 90]
n = len(numbers_to_sort)
print(numbers_to_sort, end="\n")
for i in range(n):
    for j in range(n-1):
        if numbers_to_sort[j] > numbers_to_sort[j+1]:
            buff = numbers_to_sort[j]
            numbers_to_sort[j] = numbers_to_sort[j+1]
            numbers_to_sort[j+1] = buff
print(numbers_to_sort, "\n\n")


print("Задание 4 (повышенная сложность) Построить график y=x^2 с matplotlib\n")
x = []
y = []
for i in range(-5, 6):
    x.append(i)
    y.append(i**2)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()