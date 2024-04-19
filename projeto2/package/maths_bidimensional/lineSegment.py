import math 

class LineSegment:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2
        
    def close_point(self, point, tolerance=1.1):
        distancia_ponto_segmento = self.distance_point_segment_calculator(point)
        
        distancia_pontos_segmento = math.sqrt((self._point2.x - self._point1.x) ** 2 + (self._point2.y - self._point1.y) ** 2)
        
        return distancia_ponto_segmento <= tolerance * distancia_pontos_segmento

        
    def distance_point_segment_calculator(self, point):
        x1, y1 = self._point1.x, self._point1.y
        x2, y2 = self._point2.x, self._point2.y
        x, y = point.x, point.y

        numerador = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
        denominador = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        
        return numerador / denominador
    
    def mid_point(self):
        x_media = (self._point1.x + self._point2.x) / 2
        y_media = (self._point1.y + self._point2.y) / 2
        
        return f"({x_media}, {y_media})"