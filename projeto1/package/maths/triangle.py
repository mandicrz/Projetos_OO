from package.maths.basicOperations import BasicOperations

class Triangle(BasicOperations):
    def __init__(self, base, height, a, b, c):
        self._base = base
        self._height = height
        self._a = a
        self._b = b
        self._c = c
    
    def type_of_triangle (self):
        if self._a == self._b == self._c:
            return f"Triangulo Equilatero"
        elif self._a == self._b or self._a == self._c or self._b == self._c:
            return f"Triangulo Isosceles"
        else:
            return f"Triangulo Escaleno"
        
    def area_calculator(self):
        area = (self._base * self._height) / 2
        return area
    
    def perimeter_calculator(self):
        perimeter = self._a + self._b + self._c
        return perimeter
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)