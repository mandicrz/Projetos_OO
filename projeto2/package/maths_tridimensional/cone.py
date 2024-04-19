from package.maths_tridimensional.commonOperations import commonOperations

class Cone(commonOperations):
    
    def __init__(self, raio, altura):
        self._raio = raio
        self._altura = altura
        
    def area_base(self):
        return 3.14*(self._raio)**2
    
    def area_lateral(self):
        geratriz = ((self._raio)**2 + (self._altura)**2)**0.5
        return 3.14*self._raio*geratriz
    
    def area_total(self):
        return self.area_base() + self.area_lateral()
    
    def volume(self):
        return (3.14*(self._raio)**2*self._altura)/3
    
    def perimetro(self):
        return 2*3.14*self._raio