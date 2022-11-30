class Triangle:
    num = 0
    def __init__(self, side, point):
        self.side = side
        self.point = point
        triangle.num += 1
    def perimeter(self):
        return 4 * self.side
    def area(self):
        return self.side * self.side
    def move(self, newPoint):
        oldPoint = self.point
        x = oldPoint[0] + newPoint[0]
        y = oldPoint[1] + newPoint[1]
        self.point = (x, y)
    def __str__(self):
        return "Square of {0} at {1}".format(self.side, self.point)

s1 = Triangle (8, (3, 5))
print(s1)
print("Area : ", s1.area())
print("Perimeter : ", s1.perimeter())
print("Angle 1")
print ("Angle 2")
print ("Angle 3")
s1.move((-1, 1))
print(s1)
print("Type : ", Triangle.num)
s2 = Angle (10, (-2, -6))