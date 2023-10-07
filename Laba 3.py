from math import log

x = int(input('Введите число x: '))
s_3 = int(log(x, 3))
s_5 = int(log(x, 5))
s_7 = int(log(x, 7))
for k in range(0, s_3 + 1):
    for l in range(0, s_5 + 1):
        for m in range(0, s_7 + 1):
            number = 3**k * 5**l * 7**m
            if number <= x:
                print(f'3^{k} * 5^{l} * 7^{m} = {number}')