from package.maths.basicOperations import BasicOperations

class Square(BasicOperations):
    def __init__(self, lado):
        self._lado = lado
    
    def area_calculator(self):
        area = self._lado ** 2
        return area
        
    def perimeter_calculator(self):
        perimeter = self._lado * 4
        return perimeter
    
    def diagonal_calculator(self):
        diagonal = self._lado * (2 ** 0.5)
        return diagonal
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)
    