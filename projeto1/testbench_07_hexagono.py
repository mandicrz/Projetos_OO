from package.maths_bidimensional.hexagon import Hexagon

valor_lado = 4
hexagono_teste = Hexagon(valor_lado)
area = hexagono_teste.area_calculator()
perimetro = hexagono_teste.perimeter_calculator()
soma = hexagono_teste.sum_intern_angles(6)

print(f"A area do hexagono e: {area}")
print(f"O perimetro do hexagono e: {perimetro}")
print(f"A soma dos angulos internos e: {soma}")