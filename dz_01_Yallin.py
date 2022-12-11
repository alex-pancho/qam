# Програма 1

# напишіть функцію is_square, що приймає два числа int
# повертає True якщо це квадрат, якщо ні - False

num_1, num_2 = int(input("Введіть число 'a': ")), int(input("Введіть число 'b': "))
def is_square(a,b):
    # ваш код
    kvd = a == b and a >= 0 and b >= 0
    if kvd:
        return "TRUE"
    return "FALSE"
print(is_square(num_1, num_2))

# Програма 2

# Є список дощових днів за місяць
number_of_rains = [1, 2, 3, 15, 8, 13, 21, 7, 4, 30]
# напишіть функцію, що приймає список та повертає
# інший список зі значень ["sunny", "rain"].
# Значення "sunny" присвоюється якщо було менше або рівно 5 дощових днів.

# Якщо список треба вводити вручну:
# number_of_rains = []
# num_elem_lst = int(input("Введіть кількість елементів списку: "))
# for i in range(0, num_elem_lst):
#     elem_list = int(input())
#     number_of_rains.append(elem_list)

weather_list = []
def sunny_counter(expected_list: list):
    # ваш код
    for value in number_of_rains:
        if value <= 5:
            weather_list.append("sunny")
        else:
            weather_list.append("rain")
    return weather_list
print(sunny_counter(weather_list))