from package.maths_bidimensional.basicOperations import BasicOperations
import math

class Circle (BasicOperations):
    def __init__(self, raio, center):
        self._raio = raio
        self._center = center
        
    def diameter_calculator (self):
        diameter = self._raio * 2
        return diameter
        
    def area_calculator(self):
        area = (self._raio ** 2) * 3.14
        return area
    
    def perimeter_calculator(self):
        perimeter = 2 * 3.14 * self._raio
        return perimeter
    
    def inside_point (self, point):
        distancia_centro_ponto = math.sqrt((point.x - self._center.x) ** 2 + (point.y - self._center.y) ** 2)
        
        return distancia_centro_ponto <= self._raio
    
