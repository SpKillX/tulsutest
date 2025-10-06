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