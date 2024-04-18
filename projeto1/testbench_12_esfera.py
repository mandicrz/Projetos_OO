from package.maths_tridimensional.esfera import Esfera

raio = 7.2

esfera = Esfera(raio)

area = esfera.area_total()
volume = esfera.volume()
perimetro = esfera.perimetro()
diametro = esfera.diametro()

print(f"A area total da esfera e: {area}")
print(f"O volume da esfera e: {volume}")
print(f"O perimetro da esfera e: {perimetro}")
print(f"O diametro da esfera e: {diametro}")
