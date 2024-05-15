# Дополнительное практическое задание по модулю: "Базовые структуры данных."

first_window = int(input("Введите произвольное число от 3 до 20  "))

if (first_window >= 3) and (first_window <= 20):
    print("В первом окне число: ", first_window)
    #   устанавливаем началные значения переменных
    #   первое число в паре
    second_window_1 = 1
    #   второе число в паре
    second_window_2 = 1
    #   создаем пустую строку
    result = ''

    for i in range(1, 21):
        second_window_1 = i
        for j in range(1, 21):
            second_window_2 = j
            if first_window % (second_window_1 + second_window_2) == 0:
                if second_window_1 < second_window_2:
                    result = result + str(second_window_1) + str(second_window_2)

    print("Во втором окне надо ввести пароль: ", result)

else:
    print("Вы ввели число не входящее в диапазон 3 .. 20")
