class Animal:
    def __init__(self,name):
        self.Name= name

    def info(self):
        print("Animal name:",self.Name)

class Dog(Animal):
    def sound(self):
        print(self.Name,"Barks")

d = Dog("Buddy")
d.info()
d.sound()