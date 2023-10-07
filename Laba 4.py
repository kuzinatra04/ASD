def sort(stroka):
    step = int(len(stroka) // 1.247) # От широкого гребня до мелкого
    s = 1
    while step > 1 or s > 0:
        s = 0
        i = 0

        while i + step < len(stroka):
            if stroka[i] > stroka[i+step]:
                stroka[i], stroka[i+step] = stroka[i+step], stroka[i]
                s += 1
            i += 1

        if step > 1:
            step = int(step // 1.247)

stroka = [14, 85, 654, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)

sort(stroka)
print('Отсортированный массив: ', stroka)