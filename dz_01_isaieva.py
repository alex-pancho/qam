# напишіть функцію is_square, що приймає два числа int  
# повертає True якщо це квадрат, якщо ні - False 

a = 3
b = 6
c = 3
d = 5

def is_square(one, two):
    return two == one

def is_sq(one, two):
    value_list = [one, two]
    value_list.sort()

    if is_square(value_list[0],value_list[1]):
        return "is square"
    return "is not"

print(is_sq(a,b))
print(is_sq(a,c))

# Є список дощових днів за місяць 
#number_of_rains = [1, 2, 3, 15, 8, 13, 21, 7, 4, 30]
# напишіть функцію, що прийсає сисок та повертає 
# інший список зі значень ["sunny", "rain"]. 
# Значення "sunny" присвоюється якщо було менше або рівно 5 дощових днів.

#def sunny_counter(expected_list: list):
    # ваш код
#    return ["sunny", "rain"]

number_of_rains = [1, 2, 3, 15, 8, 13, 21, 7, 4, 30]
def sunny_counter(expected_list: list):
    value_list = []
    for i in expected_list:
        if i <= 5:
            value_list.append("sunny")
        else:
            value_list.append("rain")
    return value_list

print(sunny_counter(number_of_rains))