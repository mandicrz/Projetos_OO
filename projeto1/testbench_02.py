from package.maths.lineSegment import LineSegment
from package.maths.point import Point

# Instanciando um segmento de reta
ponto1 = Point(1, 1)
ponto2 = Point(4, 4)
segmento = LineSegment(ponto1, ponto2)

# Calculando a distância entre um ponto e o segmento
ponto_teste = Point(3, 2)  # Exemplo de ponto (3, 2)
distancia = segmento.distance_point_segment_calculator(ponto_teste)
esta_proximo = segmento.close_point(ponto_teste)

# Calculando o ponto médio do segmento
ponto_medio = segmento.mid_point()

# Imprimindo os resultados
print("Distância entre o ponto (3, 2) e o segmento:", distancia)
print("Ponto médio do segmento:", ponto_medio)
print("O ponto está próximo do segmento:", esta_proximo)
