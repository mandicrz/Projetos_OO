from package.maths_tridimensional.cubo import Cubo

valor_lado = 4

cubo = Cubo(4)

areaBase = cubo.area_base()
areaLateral = cubo.area_lateral()
areaTotal = cubo.area_total()
volume = cubo.volume()
diagonal = cubo.diagonal_interna()

print(f"A area da base do cubo e: {areaBase}")
print(f"A area lateral do cubo e: {areaLateral}")
print(f"A area total do cubo e: {areaTotal}")
print(f"O volume do cubo e: {volume}")
print(f"A diagonal do cubo e: {diagonal}")