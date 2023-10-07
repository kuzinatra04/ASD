def sort(stroka):
    for i in range(len(stroka)):
        j = i - 1
        key = stroka[i]
        while stroka[j] > key and j >= 0:
            stroka[j + 1] = stroka[j]
            j -= 1

        stroka[j + 1] = key

    return stroka

stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))