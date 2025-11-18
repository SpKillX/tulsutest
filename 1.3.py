from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Сумма чисел от 1 до 10:", sum_numbers)