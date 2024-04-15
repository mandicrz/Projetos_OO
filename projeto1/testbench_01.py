from package.maths.point import Point
from package.maths.circle import Circle

# Instanciando um círculo
raio = 5
centro = Point(0, 0)  # Supondo que o centro seja (0, 0)
circulo = Circle(raio, centro)

# Calculando o diâmetro, a área e o perímetro do círculo
diametro = circulo.diameter_calculator()
area = circulo.area_calculator()
perimetro = circulo.perimeter_calculator()

# Verificando se um ponto está dentro do círculo
ponto_teste = Point(6, 0)  # Exemplo de ponto (3, 4)
esta_dentro = circulo.inside_point(ponto_teste)

# Imprimindo os resultados
print("Diâmetro do círculo:", diametro)
print("Área do círculo:", area)
print("Perímetro do círculo:", perimetro)
print("O ponto está dentro do círculo:", esta_dentro)