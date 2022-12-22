# напишіть функцію is_square, що приймає два числа int  
# повертає True якщо це квадрат, якщо ні - False 
a = 4
b = 3

a == b 

def is_square(one, two):
    result = one == two
    return result

print (is_square(3, 3))
print (is_square(a, b))

# Є список дощових днів за місяць 
number_of_rains = [1, 2, 3, 15, 8, 13, 21, 7, 4, 30]
# напишіть функцію, що прийсає сисок та повертає 
# інший список зі значень ["sunny", "rain"]. 
# Значення "sunny" присвоюється якщо було менше або рівно 5 дощових днів.
sunny_counter = ["sunny", "rain"]        
def sunny_counter(expected_list: number_of_rains):
    for sunny in number_of_rains:
        if sunny <= 5:
            print ("sunny")
        else:
            print ("rain")
    return ["sunny", "rain"]
sunny_counter (number_of_rains)
