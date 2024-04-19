from package.maths_bidimensional.basicOperations import BasicOperations
import math

class Pentagon(BasicOperations):
    def __init__(self, lado):
        self._lado = lado
    
    def area_calculator(self):
        return (5 * self._lado ** 2) / (4 * math.tan(math.pi / 5))
        
    def perimeter_calculator(self):
        perimeter = 5 * self._lado
        return perimeter
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)