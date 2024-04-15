from package.maths.basicOperations import BasicOperations

class Rectangle(BasicOperations):
    def __init__(self, base, height):
        self._base = base
        self._height = height
        
    def area_calculator(self):
        area = self._base * self._height
        return area
    
    def perimeter_calculator(self):
        perimeter = 2*(self._base + self._height)
        return perimeter
    
    def diagonal_calculator(self):
        diagonal = (self._base ** 2 + self._height ** 2) ** 0.5
        return diagonal
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)