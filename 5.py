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