def sort(stroka):
    if len(stroka) > 1:
        pivot = stroka.pop() # разделяющий элемент (крайний элемент)
        greater_lst, lst, smaller_lst = [], [pivot], [] # больше пивота, пивот, меньше пивота
        for item in stroka:
            if item == pivot:
                lst.append(item)
            elif item > pivot:
                greater_lst.append(item)
            elif item < pivot:
                smaller_lst.append(item)
        return (sort(smaller_lst) + lst + sort(greater_lst)) # для внутренних списков больше и меньше пивота делаем повторную сортировку
    else:
        return stroka


stroka = [14, 85, 654, 5, 45, 125, 74, 84, 65, 485]
print('Данный массив: ', stroka)
print('Отсортированный массив: ', sort(stroka))