# Write a class that represents a Planet. The constructor class should accept the arguments radius (in meters) and rotation_period (in seconds).
# You should implement three methods:
# (i)surface_area
# (ii)rotation_frequency
import math 
class Planet:
    def __init__(self):
        self.radius = int(input("Enter radius(in meters): "))
        self.rotation_period = int(input("Enter rotation period (in seconds): "))

    def surface_area(self):
        surface_area = (4*3.14) * ((self.radius)**2)
        print(surface_area,"Square Meters")

    def rotation_frequency(self):
        rot_frequency = (2*3.14)/(self.rotation_period)
        print(rot_frequency ,"radians per second")

        
earth = Planet()
earth.surface_area()
earth.rotation_frequency()
