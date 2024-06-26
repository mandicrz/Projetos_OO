from package.maths_bidimensional.lineSegment import LineSegment
from package.maths_bidimensional.point import Point

ponto1 = Point(1, 1)
ponto2 = Point(4, 4)
segmento = LineSegment(ponto1, ponto2)

ponto_exemplo = Point(3, 2)
distancia = segmento.distance_point_segment_calculator(ponto_exemplo)

esta_proximo = segmento.close_point(ponto_exemplo)

ponto_medio = segmento.mid_point()

print(f"O ponto 1 é: ({ponto1.x}, {ponto1.y})")
print(f"O ponto 2 é: ({ponto2.x}, {ponto2.y})")
print(f"O ponto 1 e 2 formam o segmento: ({ponto1.x}, {ponto1.y}) e ({ponto2.x}, {ponto2.y})")
print("Ponto médio do segmento:", ponto_medio)
print(f"O ponto exemplo é: ({ponto_exemplo.x}, {ponto_exemplo.y})")
print("Distância entre o ponto exemplo e o segmento:", distancia)
print("O ponto escolhido está próximo do segmento?",  esta_proximo)
