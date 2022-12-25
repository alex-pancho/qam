# напишіть функцію is_square, що приймає два числа int  
# повертає rue якщо це квадрат, якщо ні - False

def is_square():
    try:
        a = int(input("A = "))
        b = int(input("B = "))
        if a == b:
            result = "This is a square"
        else:
            result = "This is not a square"
    except:
        result = "Please, input the int value"
    return result
print("Task #1:")
print(is_square())



# Є список дощових днів за місяць 
number_of_rains = [1, 2, 3, 15, 8, 13, 21, 7, 4, 30]
# напишіть функцію, що приймає сисок та повертає
# інший список зі значень ["sunny", "rain"].
# Значення "sunny" присвоюється якщо було менше або рівно 5 дощових днів.

def sunny_counter(expected_list):
    names = ['sunny', 'rainy']
    for i in range(len(expected_list)):
        if expected_list[i]<=5:
            print(f"{expected_list[i]} — {names[0]}")
        else: print(f"{expected_list[i]} — {names[1]}")


print("\nTask #2:")
sunny_counter(number_of_rains)