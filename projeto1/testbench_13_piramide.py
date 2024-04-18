from package.maths_tridimensional.piramide import Piramide

lados = 3
altura = 4
base = 3
tipo_base = 1
altura_base = 3

piramide = Piramide(altura, base, lados, tipo_base, altura_base)

areaBase = piramide.area_base()
areaLateral = piramide.area_lateral()
areaTotal = piramide.area_total()
volume = piramide.volume()

print(f"A area da base da piramide e: {areaBase}")
print(f"A area lateral da piramide e: {areaLateral}")
print(f"A area total da piramide e: {areaTotal}")
print(f"O volume da piramide e: {volume}")
