import matplotlib.pyplot

print("Задание 4 (повышенная сложность) Построить график y=x^2 с matplotlib\n")
x = []
y = []
for i in range(-5, 6):
    x.append(i)
    y.append(i**2)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()