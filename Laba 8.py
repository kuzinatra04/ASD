def sort(stroka):
    length = len(str(max(stroka)))
    rang = 10 # переменная количества разрядов
    for i in range(length):
        arr = [] # список из пустых списков поразрядно
        for _ in range(rang):
            arr.append([])

        for x in stroka:
            figure = x // 10**i % 10
            arr[figure].append(x) # добавляем переменные в список по нумерации разряда

        stroka = [] # обнуляем строку
        for j in range(rang):
            stroka += arr[j] # добавляем в новом порядке элементы обратно в строку

    return stroka

stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))