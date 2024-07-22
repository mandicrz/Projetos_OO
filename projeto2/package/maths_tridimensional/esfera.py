from package.maths_tridimensional.commonOperations import CommonOperations
from package.maths_bidimensional.circle import Circle
class Esfera(CommonOperations):
    
    def __init__(self, raio):
        self._raio = raio
        
    def area_total(self):
        return 4*3.14*(self._raio)**2
    
    def volume(self):
        return (4*3.14*(self._raio)**3)/3
    
    def perimetro(self):
        perimetro = Circle(self._raio, 0)
        return perimetro.perimeter_calculator()
    
    def diametro(self):
        diametro = Circle(self._raio, 0)
        return diametro.diameter_calculator()    