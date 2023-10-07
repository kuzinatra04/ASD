def sort(stroka):
    for i in range(len(stroka) - 1):
        min = i
        for j in range(i + 1, len(stroka)):
            if stroka[j] < stroka[min]:
                min = j
        stroka[min], stroka[i] = stroka[i], stroka[min]

    return stroka

stroka = [14, 85, 654, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))