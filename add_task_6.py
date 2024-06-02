"""
Напишите функцию convert(L), принимающую на вход список,
состоящий из чисел и строк вида: [1, 2, '3', '4', '5', 6],
и возвращающую список целых чисел (в том же порядке): [1, 2, 3, 4, 5, 6]
"""

original_list = [1, 2, '3', '4', '5', 6]

def convert(list_):
    list_1 = []
    for i in range(len(list_)):
        if isinstance(list_[i], int):
            list_1.append(list_[i])
        else:
            list_1.append(int(list_[i]))
    return print(list_1)


convert(original_list)
