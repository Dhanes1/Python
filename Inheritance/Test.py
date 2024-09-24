class Animal:
    def __init__(self, weight):
        self.weight = weight

    def animal(self):
        animal = 0.375 * self.weight
        return animal


class Elephant(Animal):
    def info(self):
        print("Hello I'm an elephant")


class Dog(Animal):
    def info(self):
        print("Hello I'm a dog")


Elephant1 = Elephant(100)
Dog1 = Dog(10)
Dog_wim = Dog1.animal()
Elephant_wim = Elephant1.animal()
print("The Elephant weight on Mars is {}kg!".format(Elephant_wim))
print("The Dog weight on Mars is {}kg.".format(Dog_wim))