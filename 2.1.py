def compose(*functions):
    def composed(arg):
        result = arg
        for func in functions:
            result = func(result)
        return result
    return composed

def add_fifteen(x):
    return x + 15

def multiply_by_six(x):
    return x * 6

def square(x):
    return x ** 2

composed_func = compose(square, multiply_by_six, add_fifteen)
result = composed_func(3)
print("Результат композиции функций для числа 3:", result)