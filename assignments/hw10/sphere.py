"""
Sphere class
"""
import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * math.pow(self.radius,2) * math.pi

    def volume(self):
        return 4 / 3 * math.pi * math.pow(self.radius,3)