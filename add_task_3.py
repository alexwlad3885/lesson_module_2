# Дан список, состоящий из 50 элементов,
# определить сколько из них кратны 41 и
# больше (среднего арифметического максимального и минимального значений списка) значений списка.
# Для поиска максимального и минимальных значений использовать сортировку и индексы
from random import randint

def rand_list_gen(a1, a2, b):
    """
    генератор списка, заполненный случайными положительными числами
    :param a1: первый элемент диапазона чисел
    :param a2: последний элемент диапазона чисел
    :param b: количество элементов в списке
    :return: список
    """
    list_: list = []
    for i in range(b):
        list_.append(randint(a1, a2))
    return list_

def average_elm_list(max, min):
    """
    Функция подсчета среднего арифметического значений списка
    :return: значение среднего арифметического
    """

    a = 0
    a = (max + min) / 2
    return a

def max_elm_list(lst):
    """
    Функция подсчета максимального значения списка
    :param lst: анализируемый список
    :return: максимальное значение списка
    """
    lst: list
    lst.sort()
    b = lst[-1]
    return b

def min_elm_list(lst):
    """
    Функция подсчета минимального значения списка
    :param lst: анализируемый список
    :return: минимальное значение списка
    """
    lst: list
    lst.sort()
    c = lst[0]
    return c


#   создаем список, заполненный случайными положительными числами
rand_list = rand_list_gen(1, 5000, 50)

#   расчитываем максимальное значение списка
max_list = max_elm_list(rand_list)
print("Максимальное значение списка: ", max_list)

#   расчитываем минимальное значение списка
min_list = min_elm_list(rand_list)
print("Минимальное значение списка: ", min_list)

#   расчитываем среднее арифметическое значений списка
average = average_elm_list(max_list, min_list)
print("Cреднее арифметическое чисел списка: ", average)


# определяем сколько элементов списка кратны 41 и больше расчитанных значений
rand_list_wsp_multi = []
for i in rand_list:
    if i % 41 == 0:
        rand_list_wsp_multi.append(i)
rand_list_wsp_multi.sort()
multi = len(rand_list_wsp_multi)    #   список элементов кратных 41
print("Элементов списка кратных 41: ", multi)