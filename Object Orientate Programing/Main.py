class Food():
    pass
class Fruit():
    type='Food'
    def fruitmethod(self):
        print("This fruit is sweet")
Mango=Fruit()
Mango.fruitmethod()
print(Mango.type)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def stop(self):
        print("I'm a kid.")

p1 = Person("Patricia",8)

print(p1.name)
print(p1.age)
p1.stop()