from package.maths_tridimensional.cone import Cone

altura = 5
raio = 6

cone_teste = Cone(raio, altura)
areaBase = cone_teste.area_base()
areaLateral = cone_teste.area_lateral()
areaTotal = cone_teste.area_total()
volume = cone_teste.volume()
perimetro = cone_teste.perimetro()

print(f"A area da base do cone e: {areaBase}")
print(f"A area lateral do cone e: {areaLateral}")
print(f"A area total do cone e: {areaTotal}")
print(f"O volume do cone e: {volume}")
print(f"O perimetro do cone e: {perimetro}")
