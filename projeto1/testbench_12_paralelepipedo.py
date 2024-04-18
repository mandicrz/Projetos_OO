from package.maths_tridimensional.paralelepipedo import Paralelepipedo

a = 4
b = 2
c = 8

paralelepipedo = Paralelepipedo(a, b, c)
areaBase = paralelepipedo.area_base()
areaLateral = paralelepipedo.area_lateral()
areaTotal = paralelepipedo.area_total()
volume = paralelepipedo.volume()
diagonal_espacial = paralelepipedo.diagonal_interna()

print(f"A area da base do paralelepipedo e: {areaBase}")
print(f"A area lateral do paralelepipedo e: {areaLateral}")
print(f"A area total do paralelepipedo e: {areaTotal}")
print(f"O volume do paralelepipedo e: {volume}")
print(f"A diagonal do paralelepipedo e: {diagonal_espacial}")
