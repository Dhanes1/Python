class Polygon:
    def __init__ (self,sides):
        self.sides=sides

    def perimeter(self):
        perimeter=sum(self.sides)
        return perimeter
class quadrilateral(Polygon):
    def info(self):
        print("Hello this is Quadrilateral.")
class Hexagon(Polygon):
    def info(self):
        print("Hello this is hexagon")
quadrilateral1=quadrilateral([3,6,7,9])
hexagon1=Hexagon([2,2,2,2,2,2])
peri=quadrilateral1.perimeter()
hex=hexagon1.perimeter()
print("The perimeter is",peri)
print("The hexagon perimeter is",hex)