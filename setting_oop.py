
class Human:
    
    def __init__(self, name, second_name, gender):
        self.energy = 100
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

    

Miranda = Human('Miranda', 'Lendwick', 'woman')
Jack = Human('Jack', 'Daniels', 'man')
Rey = Human('Rey', 'Nielsen', 'man')
Marta = Human('Marta', 'Colins', 'woman')
Tomas = Human('Tomas', 'Defo', 'man')

Miranda.do_homework()
Miranda.talk()

Jack.sleep()
Jack.walk()
Jack.talk()

Rey.eat()
Rey.sleep()
Rey.do_homework()

Marta.eat()
Marta.walk()
Marta.talk()

Tomas.do_homework()
Tomas.walk()

humans = [Miranda, Jack, Rey, Marta, Tomas]
max_energy = 0
max_human = None
for human in humans:
    if human.energy > max_energy:
        max_energy = human.energy
        max_human = human
print(max_human.name)
        

