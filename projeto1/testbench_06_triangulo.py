from package.maths_bidimensional.triangle import Triangle

base = 3
height = 6
a = 6
b = 6
c = 3

triangulo = Triangle(base, height, a, b, c)

existencia = triangulo.triangle_exists()
forma_triangulo = triangulo.type_of_triangle()
area = triangulo.area_calculator()
perimetro = triangulo.perimeter_calculator()
soma_angulos = triangulo.sum_intern_angles(3)

print(f"A base é: ", base)
print(f"A altura é: ", height)
print(f"A lado A é: ", a)
print(f"O lado B é: ", b)
print(f"O lado C é: ", c)
print(f"O tipo do triangulo com base em sua forma é: ", forma_triangulo)
print(f"A soma dos seus angulos internos e: ", soma_angulos)
print(f"O triangulo existe?: {existencia}")