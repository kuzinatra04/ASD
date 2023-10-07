def sort(stroka):
    step = int(len(stroka) / 2)

    while step > 0:
        for i in range(step, len(stroka)):
            j = i - step
            key = stroka[i]
            while stroka[j] > key and j >= 0:
                stroka[j + step] = stroka[j]
                j -= step

            stroka[j + step] = key

        step = int(step / 2)

    return stroka

stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))
