from package.maths.rectangle import Rectangle

base = 4
height = 5

retangulo = Rectangle(base, height)

area = retangulo.area_calculator()
perimetro = retangulo.perimeter_calculator()
diagonal = retangulo.diagonal_calculator()
soma_angulos = retangulo.sum_intern_angles(4)

print(f"A base e: {base} e a altura e: {height}")
print(f"A area do retangulo e: {area}")
print(f"O perimetro do retangulo e: {perimetro}")
print(f"A diagonal do retangulo e: {diagonal}")
print(f"A soma dos angulos internos do retangulo e de: {soma_angulos}")
