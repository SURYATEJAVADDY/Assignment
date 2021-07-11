# Create a class Point and initialize with the user defined values and write a method to calculate the distance of the point from the origin.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(x,y):
        a =((x**2)+(y**2))**(0.5)
        print("Distance of the point from origin =",a)

p1 = Point.dist_from_origin(5,12)
