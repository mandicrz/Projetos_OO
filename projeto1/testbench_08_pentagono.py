from package.maths_bidimensional.pentagon import Pentagon

valor_lado = 3

pentagono = Pentagon(valor_lado)
area = pentagono.area_calculator()
perimetro = pentagono.perimeter_calculator()
somaAngulos = pentagono.sum_intern_angles(5)

print(f"A area do pentagono e: {area}")
print(f"O perimetro do pentagono e: {perimetro}")
print(f"A soma dos angulos internos e: {somaAngulos}")