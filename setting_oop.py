

class Stol():
    legs = 4
    size = 3
    def plot(self):
        return self.legs * self.size
    def boltic(self, counts):
        return self.legs * counts

class Person():
    def __init__(self, name, phone = "") -> None:
        self.name = name
        self.phone = phone
    def __repr__(self) -> str:
        return f'Person({self.name}, {self.phone})'

class Student(Person):
    course=1
    pass

if __name__ == '__main__':
    girl = Person("Daryna")
    print(girl.name)
    print(girl.phone)
    boy = Person(phone = "22-33-24", name = "Petro")
    print(boy.name)
    print(boy.phone)
    study = Student("Ivan")
    print(study)
    print(study.course)
    name = "AjsdYjnsdjk"
    print(name.upper())
    s = Stol()
    #print(s.legs)
    #
    print("Площа стола  s малого", s.plot())
    print("Стіл s на 4х ніжках треба болтіків", s.boltic(2))
    new_s = Stol()
    new_s.legs = 3
    new_s.size = 3343
    #print(new_s.legs)
    #print(new_s.size)
    print("Площа стола 'new_s'", new_s.plot())
    print("Стіл довгій 'new_s' на 3х ніжках треба болтіків", new_s.boltic(2))

