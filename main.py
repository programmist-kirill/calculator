import module
import sys

a = input('первое число: ')
b = input('второе число: ')

try:
    if a == int(a) and b == int(b):
        print('number is true')
except ValueError:
    print('неккоректные данные')
    input('нажмите enter для выхода')
    sys.exit()

print('\n\n\n\n\n1 = плюс\n2 = вычесть\n3 = умножить\n4 = разделить')
c = input('действие: ')
if c == '1':
    module.main.plus(a, b)
elif c == '2':
    module.main.minus(a, b)
elif c == '3':
    module.main.multiply(a, b)
elif c == '4':
    module.main.divide(a, b)