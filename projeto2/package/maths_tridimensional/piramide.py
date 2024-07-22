from package.maths_tridimensional.commonOperations import CommonOperations
from package.maths_bidimensional.triangle import Triangle
from package.maths_bidimensional.square import Square
from package.maths_bidimensional.pentagon import Pentagon
from package.maths_bidimensional.hexagon import Hexagon

class Piramide(CommonOperations):
    
    def __init__(self, altura, base, n_lados, altura_base):
        self._altura = altura
        self._base = base
        self._n_lados = n_lados
        self._altura_base = altura_base
        
    def area_lateral(self):
        return self._n_lados * ((self._base * self._altura)/2)
    
    def area_base(self):
        if self._n_lados == 3: #triangular
            triangulo = Triangle(self._base, self._altura_base, 0, 0, 0)
            return triangulo.area_calculator()
        if self._n_lados == 4: #quadrangular
            quadrado = Square(self._base)
            return quadrado.area_calculator()
        if self._n_lados == 5: #pentagonal
            pentagono = Pentagon(self._base)
            return pentagono.area_calculator()
        if self._n_lados == 6: #hexagonal
            hexagonal = Hexagon(self._base)
            return hexagonal.area_calculator()
    
    def area_total(self):
        return self.area_base() + self.area_lateral()
    
    def volume(self):
        return (self.area_base() * self._altura ) / 3