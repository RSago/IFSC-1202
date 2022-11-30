from math import sqrt 
from math import acos
from math import pi
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
    def type(self, newPoint):
        oldPoint = self.point
        x = oldPoint[0] + newPoint[0]
        y = oldPoint[1] + newPoint[1]
        self.point = (x, y)
    def angle(self):
        return "Angle".format(self.side, self.point)

#square length of sides 1, 2, and 3
s1 = lengthSquare(B,C)
s2 = lengthSquare(A,C)
s3 = lengthSquare(A,B)
	
# length of sides be 1, 2, 3
s1 = (float) sqrt (A)
s2 = (float) sqrt (B))
s3 = (float) sqrt (C)
	
# From Cosine law
s1 = (float) acos ((b2 + c2 - a2)/(2*b*c))
s2 = (float) acos ((a2 + c2 - b2)/(2*a*c))
s3 = (float) acos ((a2 + b2 - c2)/(2*a*b))
	
# Converting to degree
s1 = (float) (s1 * 180 / PI)
s2 = (float) (s2 * 180 / PI)
s3 = (float) (s3 * 180 / PI)

s1 = Triangle (3, (4, 5))
print(s1)
print("Area : ", s1.area())

print("Perimeter : ", s1.perimeter())
print("Angle 1")
print ("Angle 2")
print ("Angle 3")
s1.move((-1, 1))
print(s1)
print("Type : ", Triangle.num)
s2 = Angle (3, (3, 5))