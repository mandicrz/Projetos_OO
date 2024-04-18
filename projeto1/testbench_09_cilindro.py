from package.maths_tridimensional.cilindro import Cilindro

raio = 5
altura = 3 
cilindroTeste = Cilindro(raio, altura)

areaBase = cilindroTeste.area_base()
areaLateral = cilindroTeste.area_lateral()
areaTotal = cilindroTeste.area_total_calculator()
volume = cilindroTeste.volume()
perimetro = cilindroTeste.perimetro()

print(f"A area da base do cilindro e: {areaBase}")
print(f"A area lateral do cilindro e: {areaLateral}")
print(f"A area total do cilindro e: {areaTotal}")
print(f"O volume do cilindro e: {volume}")
print(f"O perimetro do cilindro e: {perimetro}")