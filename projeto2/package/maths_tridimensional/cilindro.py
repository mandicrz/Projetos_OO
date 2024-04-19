from package.maths_tridimensional.commonOperations import commonOperations

class Cilindro(commonOperations):
    
    def __init__(self, raio, altura):
        self._raio = raio
        self._altura = altura
        
    def area_base(self):
        return 3.14*(self._raio)**2
    
    def area_lateral(self):
        return 2*3.14*self._raio*self._altura
    
    def area_total_calculator(self):
        areaTotal = self.area_lateral() + 2*(self.area_base())
        return areaTotal
        
    def volume(self):
        return 3.14*(self._raio)**2 * self._altura
    
    def perimetro(self):
        return 2*3.14*self._raio