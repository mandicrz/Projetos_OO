from package.maths_bidimensional.basicOperations import BasicOperations

class Triangle(BasicOperations):
    def __init__(self, base, height, a, b, c):
        self._base = base
        self._height = height
        self._a = a
        self._b = b
        self._c = c

    
    def triangle_exists (self): 
        if (self._a + self._b > self._c) and (self._a + self._c > self._b) and (self._b + self._c > self._a):
            return True
        else:
            return False
        
    def type_of_triangle (self):
        if self._a == self._b == self._c:
            return f"Triângulo Equilátero"
        elif self._a == self._b or self._a == self._c or self._b == self._c:
            return f"Triângulo Isósceles"
        else:
            return f"Triângulo Escaleno"
        
    def area_calculator(self):
        area = (self._base * self._height) / 2
        return area
    
    def perimeter_calculator(self):
        perimeter = self._a + self._b + self._c
        return perimeter
    
    def sum_intern_angles(self, n):
        return super().sum_intern_angles(n)
    
   