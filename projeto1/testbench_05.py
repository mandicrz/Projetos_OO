from package.maths_bidimensional.square import Square

quadrado = Square (int(input("Digite o lado do quadrado: ")))

area = quadrado.area_calculator()
print("Área do quadrado:", area)

perimetro = quadrado.perimeter_calculator()
print("Perímetro do quadrado:", perimetro)

diagonal = quadrado.diagonal_calculator()
print("Diagonal do quadrado:", diagonal)

soma_angulos = quadrado.sum_intern_angles(4)
print("A soma dos angulos internos e de:", soma_angulos)