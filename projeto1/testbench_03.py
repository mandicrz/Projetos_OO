from package.maths_bidimensional.point import Point

ponto_exemplo = Point(3,4)
ponto_exemplo2 = Point(1, 4)

distancia_origem = ponto_exemplo.distance_point_origin()
distancia_pontos = ponto_exemplo.distance_points(ponto_exemplo2)

print(f"O ponto é ({ponto_exemplo.x}, {ponto_exemplo.y})")
print(f"A distancia do ponto e da origem é: {distancia_origem}")
print(f"A distancia os dois pontos é: {distancia_pontos}")
