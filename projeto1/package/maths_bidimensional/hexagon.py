from package.maths_bidimensional.basicOperations import BasicOperations
import math

class Hexagon(BasicOperations):
    def __init__(self, lado):
        self._lado = lado

    def area_calculator(self):
        return (3 * math.sqrt(3) * self._lado ** 2) / 2
        
    def perimeter_calculator(self):
        perimeter = 6 * self._lado
        return perimeter
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)
    
