def merge_list(stroka1, stroka2):
    newstroka = []
    i, j = 0, 0
    while i < len(stroka1) and j < len(stroka2): # добавляем элементы по возрастанию
        if stroka1[i] <= stroka2[j]:
            newstroka.append(stroka1[i])
            i += 1
        else:
            newstroka.append(stroka2[j])
            j += 1
    print(newstroka)

    newstroka += stroka1[i:] + stroka2[j:] # добавляем последние элементы строки 1 и 2
    return newstroka

def split_and_merge_list(stroka):
    n = len(stroka) // 2 # находим центр строки
    stroka1, stroka2 = stroka[:n], stroka[n:] # разделяем строку на две части

    if len(stroka1) > 1: # снова разделяем строку до конца первую половину
        stroka1 = split_and_merge_list(stroka1)
    if len(stroka2) > 1: # и также вторую половину
        stroka2 = split_and_merge_list(stroka2)

    return merge_list(stroka1, stroka2) # переходим к самой сортировке


stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', split_and_merge_list(stroka))
