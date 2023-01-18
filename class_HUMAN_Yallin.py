# Розробити клас Human.
# Human за замовчуванням  має: 
#     Енергію (energy) = 100
# Human при створенні повинна отримувати: 
#     Ім'я (name)
#     Прізвище (second_name)
#     Стать (gender)

# Human можуть (def):
#     Їсти     (eat) (Енергія +5)
#     Спати (sleep)  (Енергія +10)
#     Говорити (talk) (Енергія -5)
#     Ходити (walk) (Енергія -10)
#     Робити домашку (do_homework) (Енергія -90)

# Створити 3 чоловіків та 2 жінок, 
# Задати кожному з них виконання 2-3 різних дій.
# Вивести в кого найбільше енергії лишилося.

# створення класу Human із обов'язковими параметрами
class Human():
    energy = 100
    def __init__(self, name, second_name, gender) -> None:
        self.name = name
        self.second_name = second_name
        self.gender = gender
    def eat(self):
        self.energy += 5
    def sleep(self):
        self.energy += 10
    def talk(self):
        self.energy -= 5
    def walk(self):
        self.energy -= 10
    def do_homework(self):
        self.energy -= 90

J_Vitr = Human("Юліан", "Вітренко", "Male")
S_Greb = Human("Северин", "Гребенник", "Male")
Y_Kuch = Human("Йоган", "Кучеренко", "Male")
Sh_Pro = Human("Щедра", "Продан", "Female")
D_Dan = Human("Донна", "Данильчук", "Female")

J_Vitr.eat()
J_Vitr.sleep()
J_Vitr.talk()

S_Greb.sleep()
S_Greb.talk()
S_Greb.walk()

Y_Kuch.talk()
Y_Kuch.walk()
Y_Kuch.do_homework()

Sh_Pro.walk()
Sh_Pro.do_homework()
Sh_Pro.eat()

D_Dan.do_homework()
D_Dan.eat()
D_Dan.sleep()

lemings = [J_Vitr, S_Greb, Y_Kuch, Sh_Pro, D_Dan]
max_eng = 0
max_lem = None
for k in lemings:
    if k.energy > max_eng:
        max_eng = k.energy
        max_lem = k.name + " " + k.second_name

print(max_lem, "має максимальне значення енергії: ", max_eng)





