# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


lst_equation = equation.split()
index_x = float(lst_equation[2].replace('x', '')) * x
y = index_x + float(lst_equation[4])

print(y)
