class Car:
    def __init__(self,Type,Color):
        self.Type = Type
        self.Color = Color
    def stop(self):
        print("The {} is stopped.".format(self.Type))
    def on(self):
        print("This car's engine have been turned on.")

Car1=Car("Jeep","Blue")
Car2=Car("Premium car","Yellow")

print(Car1.Type)
print(Car2.Type)
Car1.stop()
Car2.stop()