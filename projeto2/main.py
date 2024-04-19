from package.maths_bidimensional import *
from package.maths_tridimensional import *

print("Bem vindo(a), esse é um programa para criar figuras geométricas. Escolha qual quer formar: ")

print("|1|. Figuras Adimensionais")
print("|2|. Figuras Bidimensionais")
print("|3|. Figuras Tridimensionais")
print("|4|. Sair")

option = input()

if option == "1":
    while True:
        print("|1|. Ponto")
        print("|2|. Segmento de Reta")
        print("|3|. Sair")
            
        option1 = input()
        
        if option1 == "3":
            break
            
        if option1 == "1":
            while True:
                print("Você escolheu criar um ponto, digite suas coordenadas separadas por vírgula: ")

                coordenadas = input().split(",")
                x = float(coordenadas[0])
                y = float(coordenadas[1])

                ponto1 = Point(x, y)

                print(f"O ponto criado foi: ({ponto1.x}, {ponto1.y})")
                
                print("Escolha entre as opções a seguir:")
                print("|1|. Distância da Origem")
                print("|2|. Criar outro ponto")
                print("|3|. Sair")
                
                option1_1 = input()
                
                if option1_1 == "1":
                        print(f"A distância do ponto ({ponto1.x}, {ponto1.y}) até a origem é: {ponto1.distance_point_origin()}")
                        break
                if option1_1 == "2":
                        print("Digite as coordenadas do outro ponto: ")
                        coordenadas2 = input().split(",")
                        x2 = float(coordenadas2[0])
                        y2 = float(coordenadas2[1])
                        
                        ponto2 = Point(x2, y2)
                        
                        print(f"O segundo ponto criado foi: ({ponto2.x}, {ponto2.y}), e sua distância do primeiro ponto ({ponto1.x}, {ponto1.y}) é: {ponto1.distance_points(ponto2)}")
                        break
                else:
                    break
        
        if option1 == "2":
            while True:
                print("Você escolheu criar um segmento de reta, digite o primeiro ponto: ")
                coordenadas = input().split(",")
                x = float(coordenadas[0])
                y = float(coordenadas[1])
                ponto1 = Point(x, y)
                
                print("Digite o segundo: ")
                coordenadas2 = input().split(",")
                x2 = float(coordenadas2[0])
                y2 = float(coordenadas2[1])
                ponto2 = Point(x2, y2)
                
                segmento = LineSegment(ponto1, ponto2)
                
                print("Escolha entre as opções a seguir: ")                
                print("|1|. Distância de um ponto qualquer ao segmento")
                print("|2|. Verificar se um ponto qualquer está perto do segmento")
                print("|3|. Ponto médio do segmento")
                print("|4|. Sair")

                option1_2 = input()
                
                if option1_2 == "1":
                    print("Digite o ponto que quer comparar: ")
                    coordenadas3 = input().split(",")
                    x3 = float(coordenadas3[0])
                    y3 = float(coordenadas3[1])
                    ponto3 = Point(x3, y3)
                    
                    print(f"O ponto ({ponto3.x}, {ponto3.y}) está a uma distância de {segmento.distance_point_segment_calculator(ponto3)}")
                    break                      
                 
                if option1_2 == "2":
                    print("Digite um ponto que quer verificar: ")
                    coordenadas3 = input().split(",")
                    x3 = float(coordenadas3[0])
                    y3 = float(coordenadas3[1])
                    ponto3 = Point(x3, y3)
                    
                    if segmento.close_point(ponto3):
                        print(f"O ponto ({ponto3.x}, {ponto3.y}) está perto do segmento!)")
                    else:
                        print(f"O ponto ({ponto3.x}, {ponto3.y}) não está perto do segmento!")
                    break
                
                if option1_2 == "3":
                    print(f"O ponto médio do segmento é: {segmento.mid_point()}")
                    break
            
        else:
            break

      