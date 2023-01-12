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
    def __init__(self, name = "", second_name = "", gender = "") -> None:
        self.name = name
        self.second_name = second_name
        self.gender = gender
    def __repr__(self) -> str:
        return f'{self.name} {self.second_name}, {self.gender};'
  
# створення класу Активностей із дельтою енергиї
class Activity():
    eat = 5
    sleep = 10
    talk = -5
    walk = -10
    do_homework = -90
    pass

# функція підрахунку загальної енергії виходячи з обраних активностей. при відсутності активності, параметр = 0
def human_energy(act_1 = 0, act_2 = 0, act_3 = 0, act_4 = 0, act_5 = 0):
    result_energy = Human.energy + act_1 + act_2 + act_3 + act_4 + act_5
    return result_energy

class Lemming_1(Human):
    name = "Юліан"
    second_name = "Вітренко"
    gender = "Male"
    act1 = Activity.eat
    act2 = Activity.sleep
    act3 = Activity.talk
    pass

class Lemming_2(Human):
    name = "Северин"
    second_name = "Гребенник"
    gender = "Male"
    act1 = Activity.sleep
    act2 = Activity.talk
    act3 = Activity.walk
    pass

class Lemming_3(Human):
    name = "Йоган"
    second_name = "Кучеренко"
    gender = "Male"
    act1 = Activity.talk
    act2 = Activity.walk
    act3 = Activity.do_homework
    pass

class Lemming_4(Human):
    name = "Щедра"
    second_name = "Продан"
    gender = "Female"
    act1 = Activity.walk
    act2 = Activity.do_homework
    act3 = Activity.eat
    pass

class Lemming_5(Human):
    name = "Донна"
    second_name = "Данильчук"
    gender = "Female"
    act1 = Activity.do_homework
    act2 = Activity.eat
    act3 = Activity.sleep
    pass
# функція визначення максимальної енергії у Лемінга
def max_energy(a, b, c, d, e):
    hero = max(a, b, c, d, e)
    if hero == a:
        return f'{Lemming_1.name} {Lemming_1.second_name} - {hero}'
    elif hero == b:
        return f'{Lemming_2.name} {Lemming_2.second_name} - {hero}'
    elif hero == c:
        return f'{Lemming_3.name} {Lemming_3.second_name} - {hero}'
    elif hero == d:
        return f'{Lemming_4.name} {Lemming_4.second_name} - {hero}'
    else:
        return f'{Lemming_5.name} {Lemming_5.second_name} - {hero}'

if __name__ == '__main__':
    # розрахунок енергії після вибраних активностей Лемінгів
    health_1 = human_energy(Lemming_1.act1, Lemming_1.act2, Lemming_1.act3)
    health_2 = human_energy(Lemming_2.act1, Lemming_2.act2, Lemming_2.act3)
    health_3 = human_energy(Lemming_3.act1, Lemming_3.act2, Lemming_3.act3)
    health_4 = human_energy(Lemming_4.act1, Lemming_4.act2, Lemming_4.act3)
    health_5 = human_energy(Lemming_5.act1, Lemming_5.act2, Lemming_5.act3)
    spis_health = max_energy(health_1, health_2, health_3, health_4, health_5)
    
print("Максимально енергії залишилось у:", spis_health, "поінтів;")

# print("1. ", Human(Lemming_1.name, Lemming_1.second_name, Lemming_1.gender), "Залишок енергії: ", health_1) 
# print("2. ", Human(Lemming_2.name, Lemming_2.second_name, Lemming_2.gender), "Залишок енергії: ", health_2)
# print("3. ", Human(Lemming_3.name, Lemming_3.second_name, Lemming_3.gender), "Залишок енергії: ", health_3)
# print("4. ", Human(Lemming_4.name, Lemming_4.second_name, Lemming_4.gender), "Залишок енергії: ", health_4)
# print("5. ", Human(Lemming_5.name, Lemming_5.second_name, Lemming_5.gender), "Залишок енергії: ", health_5)
