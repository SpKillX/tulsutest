def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Первые 10 чисел Фибоначчи:")
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")
print()