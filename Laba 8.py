def sort(stroka):
    max = stroka[0]
    for i in range(1, len(stroka)):
        if stroka[i] > max:
            max = stroka[i]

    kolvo = len(str(max))

    elements = []
    for i in stroka:
        digits = []
        while i > 0:
            digits.append(i % 10)
            i = i // 10
        digits.extend((kolvo - len(digits)) * [0])
        elements.append(digits)

    print(elements)

    for k in range(kolvo):
        for i in range(len(elements) - 1):
            min = i
            for j in range(i + 1, len(elements)):
                if elements[j][k] < elements[min][k]:
                    min = j
            elements[min], elements[i] = elements[i], elements[min]

        print(elements)

    for i, strochka in enumerate(elements):
        strochka.reverse()
        tmp = ''
        for s in strochka:
            tmp += str(s)
        elements[i] = int(tmp)

    return elements


stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))
