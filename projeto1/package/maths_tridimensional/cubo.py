from package.maths_tridimensional.commonOperations import commonOperations

class Cubo(commonOperations):
    
    def __init__(self, aresta):
        self._aresta = aresta
        
    def area_base(self):
        return (self._aresta)**2
    
    def area_lateral(self):
        return 4*(self._aresta)**2
    
    def area_total(self):
        return 2*(self.area_base()) + self.area_lateral()
    
    def volume(self):
        return (self._aresta)**3
    
    def diagonal_interna(self):
        return self._aresta*(3)**0.5