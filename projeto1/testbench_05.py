from package.maths.square import Square

# Criando um objeto Square com lado igual a 5
quadrado = Square (int(input("Digite o lado do quadrado")))

# Calculando e imprimindo a área do quadrado
print("Área do quadrado:", quadrado.area_calculator())

# Calculando e imprimindo o perímetro do quadrado
print("Perímetro do quadrado:", quadrado.perimeter_calculator())

# Calculando e imprimindo a diagonal do quadrado
print("Diagonal do quadrado:", quadrado.diagonal_calculator())

print("Soma dos angulos internos e", quadrado.sum_intern_angles())