from package.maths.point import Point
from package.maths.circle import Circle

# Instanciando um círculo

raio = 5
centro = Point(0, 0)
circulo = Circle(raio, centro)

# Calculando o diâmetro, a área e o perímetro do círculo

diametro = circulo.diameter_calculator()
area = circulo.area_calculator()
perimetro = circulo.perimeter_calculator()

# Verificando se um ponto está dentro do círculo

ponto_exemplo = Point(6, 0)  # Exemplo de ponto (3, 4)
esta_dentro = circulo.inside_point(ponto_exemplo)

# Imprimindo os resultados
print("A raio do circulo e:", raio)
print(f"O centro do circulo e: ({centro.x}, {centro.y})") 
print("Diâmetro do círculo:", diametro)
print("Área do círculo:", area)
print("Perímetro do círculo:", perimetro)
print(f"Ponto exemplo:, ({ponto_exemplo.x}, {ponto_exemplo.y})")
print("O ponto está dentro do círculo?", esta_dentro)