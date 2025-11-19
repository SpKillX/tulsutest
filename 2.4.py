def filter_numbers_from_file(filename, condition):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    try:
                        number = float(word)
                        if condition(number):
                            yield number
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

print("Четные числа из файла:")
even_numbers = filter_numbers_from_file('numbers.txt', lambda x: x % 2 == 0 and x > 0)
for num in even_numbers:
    print(num, end=" ")
print()

print("Положительные числа из файла:")
positive_numbers = filter_numbers_from_file('numbers.txt', lambda x: x > 0)
for num in positive_numbers:
    print(num, end=" ")
print()