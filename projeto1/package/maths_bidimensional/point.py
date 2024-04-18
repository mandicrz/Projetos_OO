import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance_point_origin(self):
        distancia_ponto_origem = math.sqrt((0 - self.x)**2 + (0 - self.y)**2)
        return distancia_ponto_origem
    
    def distance_points(self, point):
        x2 = point.x
        y2 = point.y
        distancia_pontos = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        return distancia_pontos
    
