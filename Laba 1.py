def check(stroka):
    stack = []
    open = ['(', '{', '[']
    close = [')', '}', ']']

    for element in stroka:
        if element in open:
            stack.append(element)

        elif element in close:

            if len(stack) == 0:
                return 'Строка не существует'

            last_open = stack.pop()
            if open.index(last_open) != close.index(element):
                return 'Строка не существует'


    if len(stack) != 0:
        return 'Строка не существует'

    else:
        return 'Строка существует'

stroka = input('Введите строку: ')
print(check(stroka))