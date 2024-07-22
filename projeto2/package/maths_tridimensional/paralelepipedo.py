from package.maths_tridimensional.commonOperations import CommonOperations

class Paralelepipedo(CommonOperations):
    
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    def area_base(self):
        return self._a * self._b
    
    def area_lateral(self):
        return self._a * self._c + self._c * self._b
    
    def area_total(self):
        return 2*(self.area_base()) + 2*(self.area_lateral())
    
    def volume(self):
        return self._a * self._b * self._c
    
    def diagonal_interna(self):
        return ((self._a)**2 + (self._b)**2 + (self._c)**2)**0.5
    
    