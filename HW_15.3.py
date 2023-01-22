class Stydent():
    def __init__(self, name , second_name , gender ):
        self.energy = 100
        self.name = name
        self.second_name = second_name
        self.gender = gender
    def __repr__(self) -> str:
        return f'({self.name}, {self.second_name}, {self.gender})'

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
    def check_homework(self): #Довелося додати ще одну функцію для реалістичності
        self.energy -= 45

#Вирішив зробити список із відомих нам людей)

Alex = Stydent('Alex', 'Panchenko', 'man')
Aleksey = Stydent('Aleksey', 'Yallin', 'man')
Ihor = Stydent('Ihor', 'Torosyan', 'man' )
Ruslana = Stydent('Ruslana', 'Mudrast', 'woman')
Anna = Stydent('Anna', 'Isaeva', 'woman')

Alex.eat()
Alex.talk()
Alex.check_homework()

Aleksey.eat()
Aleksey.talk()
Aleksey.do_homework()

Ihor.eat()
Ihor.sleep()

Ruslana.eat()
Ruslana.talk()
Ruslana.do_homework()

Anna.eat()
Anna.walk()
Anna.do_homework()

Stydents = [ Alex, Aleksey, Ihor, Ruslana, Anna]
max_energy = 0
max_Stydent = None
for Stydent in Stydents:
    if Stydent.energy > max_energy:
        max_energy = Stydent.energy
        max_Stydent = Stydent
        print (max_Stydent.name)