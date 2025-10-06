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

number = 5
if number < 0:
    print("Введите неотрицательное число\n")
elif number == 0:
    print("Факториал числа 0 равен ", 1, "\n")
else:
    print(f"Факториал числа {number} равен {factorial(number)}\n")


print("Задание 5 Список простых чисел до 100\n")
for numbers in range(2, 101):
    is_prime = True
    for i in range(2, int(numbers**0.5)+1):
        if numbers % i == 0:
            is_prime = False
            break
    if is_prime:
        print(numbers, end=" ")
print("\n\n")


print("Задание 1 (повышенная сложность) Сортировка списка пузырьком\n")
list = [15, 35, 78, 1, 2, 64, 34, 25, 12, 22, 11, 90]
n = len(list)
print(list, end="\n")
for i in range(n):
    for j in range(n-1):
        if list[j] > list[j+1]:
            buff = list[j]
            list[j] = list[j+1]
            list[j+1] = buff
print(list, "\n\n")


