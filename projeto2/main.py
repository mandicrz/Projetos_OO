from package.maths_bidimensional import *
from package.maths_tridimensional import *

def main():
    while True: 
        print("Bem vindo(a), esse e um programa para criar figuras geometricas. Escolha qual quer formar: ")
        print("Atente-se: A medida de grandeza das formas esta definida em metros, metros quadrados(areas) e metros cubicos(volume)!")

        print("|1|. Figuras Adimensionais")
        print("|2|. Figuras Bidimensionais")
        print("|3|. Figuras Tridimensionais")
        print("|4|. Sair")

        option = input()

        if option == "1":
            while True:
                print("|1|. Ponto")
                print("|2|. Segmento de Reta")
                print("|3|. Voltar")
                    
                option1 = input()
                
                if option1 == "1":
                    while True:
                        print("Voce escolheu criar um ponto! Digite suas coordenadas (separadas por virgula): ")

                        coordenadas = input("Ponto: ").split(",")
                        x = float(coordenadas[0])
                        y = float(coordenadas[1])

                        ponto1 = Point(x, y)

                        print(f"O ponto criado foi: ({ponto1.x}, {ponto1.y})")
                        
                        while True:
                            print("Escolha entre as opcoes a seguir:")
                            print("|1|. Distancia da Origem")
                            print("|2|. Criar outro ponto")
                            print("|3|. Voltar")
                            
                            option1_1 = input()
                            
                            if option1_1 == "1":
                                print(f"A distancia do ponto ({ponto1.x}, {ponto1.y}) ate a origem e: {ponto1.distance_point_origin()}")
                                
                            elif option1_1 == "2":
                                print("Digite as coordenadas do outro ponto: ")
                                coordenadas2 = input("Ponto 2: ").split(",")
                                x2 = float(coordenadas2[0])
                                y2 = float(coordenadas2[1])
                                    
                                ponto2 = Point(x2, y2)
                                    
                                print(f"O segundo ponto criado foi: ({ponto2.x}, {ponto2.y}), e sua distancia do primeiro ponto ({ponto1.x}, {ponto1.y}) e: {ponto1.distance_points(ponto2)}")
                                
                            
                            elif option1_1 == "3":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                    
                        
                
                elif option1 == "2":
                    while True:
                        print("Voce escolheu criar um segmento de reta! Digite o primeiro ponto (x e y separados por virgula): ")
                        coordenadas = input("Primeiro ponto: ").split(",")
                        x = float(coordenadas[0])
                        y = float(coordenadas[1])
                        ponto1 = Point(x, y)
                        
                        print("Digite o segundo: ")
                        coordenadas2 = input("Segundo ponto: ").split(",")
                        x2 = float(coordenadas2[0])
                        y2 = float(coordenadas2[1])
                        ponto2 = Point(x2, y2)
                        
                        segmento = LineSegment(ponto1, ponto2)
                        
                        while True: 
                            print("Escolha entre as opcoes a seguir: ")                
                            print("|1|. Distancia de um ponto qualquer ao segmento")
                            print("|2|. Verificar se um ponto qualquer esta perto do segmento")
                            print("|3|. Ponto medio do segmento")
                            print("|4|. Voltar")

                            option1_2 = input()
                            
                            if option1_2 == "1":
                                print("Digite o ponto que quer comparar: ")
                                coordenadas3 = input("Ponto: ").split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                print(f"O ponto ({ponto3.x}, {ponto3.y}) esta a uma distancia de {segmento.distance_point_segment_calculator(ponto3)}")
                                                    
                            
                            elif option1_2 == "2":
                                print("Digite um ponto que quer verificar: ")
                                coordenadas3 = input("Ponto: ").split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                if segmento.close_point(ponto3):
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) esta perto do segmento!")
                                    
                                else:
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) nao esta perto do segmento!")
                                
                            
                            elif option1_2 == "3":
                                print(f"O ponto medio do segmento e: {segmento.mid_point()}")
                                
                            elif option1_2 == "4":
                                break
                            
                            else: 
                                print("Valor incorreto!")
                        break
                            
                elif option1 == "3":
                    break
                
                else:
                    print("Valor incorreto!")

        if option == "2":
            while True:
                print("|1|. Circulo")
                print("|2|. Hexagono")
                print("|3|. Pentagono")
                print("|4|. Retangulo")
                print("|5|. Quadrado")
                print("|6|. Triangulo")
                print("|7|. Voltar")
                
                option2 = input()
                
                if option2 == "1":
                    while True:
                        print("Voce escolheu criar um circulo! Digite o raio e o centro (x e y separados por virgula) do mesmo (separados por enter):")
                        
                        raio = float(input("Raio: "))
                        circle = input("Centro: ").split(",")
                        x = float(circle[0])
                        y = float(circle[1])
                        
                        centro = Point(x, y)
                        circulo = Circle(raio, centro)
                        
                        while True: 
                            print("Escolha entre as opcoes a seguir: ")
                            print("|1|. Diametro")
                            print("|2|. Area")
                            print("|3|. Perimetro")
                            print("|4|. Verificar se um ponto qualquer esta dentro do circulo")
                            print("|5|. Voltar")
                            
                            option2_1 = input()
                            
                            if option2_1 == "1":
                                print(f"O diametro do circulo de raio e: {circulo.diameter_calculator()}")
                                
                                
                            elif option2_1 == "2":
                                print(f"A area do circulo de raio e: {circulo.area_calculator()}")
                                
                                
                            elif option2_1 == "3":
                                print(f"O perimetro do circulo de raio e: {circulo.perimeter_calculator()}")
                                
                            elif option2_1 == "4":
                                print("Digite o ponto que quer verificar (x e y separados por virgula): ")
                                ponto = input("Ponto: ").split(",")
                                x2 = float(ponto[0])
                                y2 = float(ponto[1])
                                    
                                ponto = Point(x2, y2)
                                    
                                if circulo.inside_point(ponto):
                                    print(f"O ponto ({ponto.x}, {ponto.y}) esta dentro do circulo")
                                else:
                                    print(f"O ponto ({ponto.x}, {ponto.y}) nao esta dentro do circulo")
                                
                            elif option2_1 == "5":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                    
                elif option2 == "2": 
                    while True:
                        print("Voce escolheu criar um hexagono! Digite a medida de seu lado: ")
                        hexagono = Hexagon(float(input("Lado: ")))

                        while True:
                            print("Escolha entre as opcoes a seguir: ")
                            print("|1|. Area")
                            print("|2|. Perimetro")
                            print("|3|. Soma dos angulos internos")
                            print("|4|. Voltar")
                            
                            option2_2 = input()
                            
                            if option2_2 == "1":
                                print(f"A area do hexagono e: {hexagono.area_calculator()}")

                            elif option2_2 == "2":
                                print(f"O perimetro do hexagono e: {hexagono.perimeter_calculator()}")
                            
                            elif option2_2 == "3":
                                print(f"A soma dos angulos internos do hexagono e: {hexagono.sum_intern_angles(6)}°")
                                
                            elif option2_2 == "4":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                
                elif option2 == "3":
                    while True:
                        print("Voce escolheu criar um pentagono! Digite a medida de seu lado: ")
                        pentagono = Pentagon(float(input("Lado: ")))   
                        
                        while True: 
                            print("Escolha entre as opcoes a seguir: ")
                            print("|1|. Area")
                            print("|2|. Perimetro")
                            print("|3|. Soma dos angulos internos")
                            print("|4|. Voltar")
                            
                            option2_3 = input()
                            
                            if option2_3 == "1":
                                print(f"A area do pentagono e: {pentagono.area_calculator()}")

                            elif option2_3 == "2":
                                print(f"O perimetro do pentagono e: {pentagono.perimeter_calculator()}")
                            
                            elif option2_3 == "3":
                                print(f"A soma dos angulos internos do pentagono e: {pentagono.sum_intern_angles(5)}°")
                                
                            elif option2_3 == "4":
                                break
                            
                            else: 
                                print("Valor incorreto!")
                                                            
                        break
                    
                elif option2 == "4":
                    while True: 
                        print("Voce escolheu criar um retangulo! Digite sua base e altura (seguidos por enter): ")
                        base = float(input("Base: "))
                        altura = float(input("Altura: "))
                        retangulo = Rectangle(base, altura)
                        
                        while True: 
                            print("Escolha entre as opcoes a seguir: ")
                            print("|1|. Area")
                            print("|2|. Perimetro")
                            print("|3|. Diagonal")
                            print("|4|. Soma dos angulos internos")
                            print("|5|. Voltar")
                            
                            option2_4 = input()
                            
                            if option2_4 == "1":
                                print(f"A area do retangulo e: {retangulo.area_calculator()}")

                            elif option2_4 == "2":
                                print(f"O perimetro do retangulo e: {retangulo.perimeter_calculator()}")
                            
                            elif option2_4 == "3": 
                                print(f"A diagonal do retangulo e: {retangulo.diagonal_calculator()}")
                                
                            elif option2_4 == "4":
                                print(f"A soma dos angulos internos do retangulo e: {retangulo.sum_intern_angles(4)}°")
                                
                            elif option2_4 == "5":
                                break     
                            
                            else: 
                                print("Valor incorreto!")     
                               
                        break
                elif option2 == "5":
                    while True: 
                        print("Voce escolheu criar um quadrado! Digite a medida de seu lado: ")
                        quadrado = Square(float(input("Lado: ")))   
                        
                        while True: 
                            print("Escolha entre as opcoes a seguir: ")
                            print("|1|. Area")
                            print("|2|. Perimetro")
                            print("|3|. Diagonal")
                            print("|4|. Soma dos angulos internos")
                            print("|5|. Voltar")
                            
                            option2_5 = input()
                            
                            if option2_5 == "1":
                                print(f"A area do quadrado e: {quadrado.area_calculator()}")

                            elif option2_5 == "2":
                                print(f"O perimetro do quadrado e: {quadrado.perimeter_calculator()}")
                            
                            elif option2_5 == "3": 
                                print(f"A diagonal do quadrado e: {quadrado.diagonal_calculator()}")
                                
                            elif option2_5 == "4":
                                print(f"A soma dos angulos internos do quadrado e: {quadrado.sum_intern_angles(4)}°")
                                
                            elif option2_5 == "5":
                                break 
                            
                            else: 
                                print("Valor incorreto!")
                                         
                        break
                    
                elif option2 == "6":
                    while True: 
                        print("Voce escolheu criar um triangulo! Digite a sua base e sua altura (separados por enter): ")
                        base = float(input("Base: "))
                        altura = float(input("Altura: "))
                        
                        print("Digite agora a medida de seus lados (separados por enter): ")
                        a = float(input("Lado A: "))
                        b = float(input("Lado B: "))
                        c = float(input("Lado C: "))
                        
                        triangulo = Triangle(base, altura, a, b, c)  
                        
                        if triangulo.triangle_exists(): 
                            while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area")
                                print("|2|. Perimetro")
                                print("|3|. Soma dos angulos internos")
                                print("|4|. Tipo de triangulo com base em seus lados")
                                print("|5|. Voltar")
                                
                                option2_6 = input()

                                if option2_6 == "1":
                                    print(f"A area do triangulo e: {triangulo.area_calculator()}")

                                elif option2_6 == "2":
                                    print(f"O perimetro do triangulo e: {triangulo.perimeter_calculator()}")
                                    
                                elif option2_6 == "3":
                                    print(f"A soma dos angulos internos do triangulo e: {triangulo.sum_intern_angles(3)}°")
                                    
                                elif option2_6 == "4":
                                    print(triangulo.type_of_triangle())
                                    
                                elif option2_6 == "5":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                                    
                            break
                        else:
                            print("O triangulo informado nao atende aos requisitos de criacao. Digite novos valores: ")
                
                elif option2 == "7":
                    break   
                
                else:
                    print("Valor incorreto!")    
            
                              
        elif option == "3":
            while True:
                print("|1|. Cilindro")
                print("|2|. Cone")
                print("|3|. Cubo")
                print("|4|. Esfera")
                print("|5|. Paralelepipedo")
                print("|6|. piramide")
                print("|7|. Voltar")
                
                option3 = input()
                
                if option3 == "1":
                    while True:
                        print("Voce escolheu criar um cilindro! Digite a sua raio e sua altura (separados por enter): ")
                        
                        raio = float(input("Raio: "))
                        altura = float(input("Altura: "))
                        
                        cilindro = Cilindro(raio, altura)
                        
                        while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area da Base")
                                print("|2|. Area Lateral")
                                print("|3|. Area Total")
                                print("|4|. Volume")
                                print("|5|. Perimetro")
                                print("|6|. Voltar")
                                
                                option3_1 = input()
                                
                                if option3_1 == "1":
                                    print(f"A area da base do cilindro e: {cilindro.area_base()}")
                                    
                                elif option3_1 == "2":
                                    print(f"A area lateral do cilindro e: {cilindro.area_lateral()}")
                                    
                                elif option3_1 == "3":
                                    print(f"A area total do cilindro e: {cilindro.area_total()}")  
                                    
                                elif option3_1 == "4":
                                    print(f"O volume do cilindro e: {cilindro.volume()}")
                                     
                                elif option3_1 == "5":
                                    print(f"O perimetro do cilindro e: {cilindro.perimetro()}")
                                    
                                elif option3_1 == "6":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                        break 
                        
                elif option3 == "2": 
                    while True:
                        print("Voce escolheu criar um cone! Digite a sua raio e sua altura (separados por enter): ")
                        
                        raio = float(input("Raio: "))
                        altura = float(input("Altura: "))
                        
                        cone = Cone(raio, altura)
                        
                        while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area da Base")
                                print("|2|. Area Lateral")
                                print("|3|. Area Total")
                                print("|4|. Volume")
                                print("|5|. Perimetro")
                                print("|6|. Voltar")
                                
                                option3_2 = input()
                                
                                if option3_2 == "1":
                                    print(f"A area da base do cone e: {cone.area_base()}")
                                    
                                elif option3_2 == "2":
                                    print(f"A area lateral do cone e: {cone.area_lateral()}")
                                    
                                elif option3_2 == "3":
                                    print(f"A area total do cone e: {cone.area_total()}") 
                                        
                                elif option3_2 == "4":
                                    print(f"O volume do cone e: {cone.volume()}") 
                                    
                                elif option3_2 == "5":
                                    print(f"O perimetro do cone e: {cone.perimetro()}")
                                    
                                elif option3_2 == "6":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                        break 
        
                elif option3 == "3":
                    while True:
                        print("Voce escolheu criar um cubo! Digite a medida da aresta: ")
                        
                        cubo = Cubo(float(input("Aresta: ")))
                        
                        while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area da Base")
                                print("|2|. Area Lateral")
                                print("|3|. Area Total")
                                print("|4|. Volume")
                                print("|5|. Diagonal Espacial")
                                print("|6|. Voltar")
                                
                                option3_3 = input()
                                
                                if option3_3 == "1":
                                    print(f"A area da base do cubo e: {cubo.area_base()}")
                                    
                                elif option3_3 == "2":
                                    print(f"A area lateral do cubo e: {cubo.area_lateral()}")
                                    
                                elif option3_3 == "3":
                                    print(f"A area total do cubo e: {cubo.area_total()}") 
                                     
                                elif option3_3 == "4":
                                    print(f"O volume do cubo e: {cubo.volume()}") 
                                    
                                elif option3_3 == "5":
                                    print(f"A diagonal espacial do cubo e: {cubo.diagonal_interna()}")
                                    
                                elif option3_3 == "6":
                                    break
                                
                                else: 
                                    print("Valor incorreto!")
                        break 
                    
                elif option3 == "4":
                    while True: 
                        print("Voce escolheu criar uma esfera! Digite o raio da mesma: ")
                        
                        esfera = Esfera(float(input("Raio: ")))
                        
                        while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area Total")
                                print("|2|. Volume")
                                print("|3|. Perimetro")
                                print("|4|. Diametro")
                                print("|5|. Voltar")
                                
                                option3_4 = input()
                                
                                if option3_4 == "1":
                                    print(f"A area total da esfera e: {esfera.area_total()}")
                                    
                                elif option3_4 == "2":
                                    print(f"O volume da esfera e: {esfera.volume()}")
                                    
                                elif option3_4 == "3":
                                    print(f"O perimetro da esfera e: {esfera.perimetro()}") 
                                     
                                elif option3_4 == "4":
                                    print(f"O diametro da esfera e: {esfera.diametro()}")
                                    
                                elif option3_4 == "5":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                                    
                        break 
                
                elif option3 == "5":
                    while True: 
                        print("Voce escolheu criar um paralelepipedo! Digite a medida da largura, comprimento e altura (separadas por enter): ")
                        
                        largura = float(input("Largura: "))
                        comprimento = float(input("Comprimento: "))
                        altura = float(input("Altura: "))
                        
                        paralelepipedo = Paralelepipedo(largura, comprimento, altura)
                        
                        while True: 
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area da Base")
                                print("|2|. Area Lateral")
                                print("|3|. Area Total")
                                print("|4|. Volume")
                                print("|5|. Diagonal Espacial")
                                print("|6|. Voltar")
                                
                                option3_5 = input()
                                
                                if option3_5 == "1":
                                    print(f"A area da base do paralelepipedo e: {paralelepipedo.area_base()}")
                                    
                                elif option3_5 == "2":
                                    print(f"A area lateral do paralelepipedo e: {paralelepipedo.area_lateral()}")
                                    
                                elif option3_5 == "3":
                                    print(f"A area total do paralelepipedo e: {paralelepipedo.area_total()}") 
                                     
                                elif option3_5 == "4":
                                    print(f"O volume do paralelepipedo e: {paralelepipedo.volume()}")
                                    
                                elif option3_5 == "5":
                                    print(f"A diagonal espacial do paralelepipedo e: {paralelepipedo.diagonal_interna()}")
                                    
                                elif option3_5 == "6":
                                    break
                                
                                else: 
                                    print("Valor incorreto!")
                                    
                        break 
                
                elif option3 == "6":
                    while True:
                        print("Voce escolheu criar uma piramide, digite as medidas da altura e da base e o numero de lados da mesma, de 3 a 6 (separadas por enter):")
                        
                        altura = float(input("Altura: "))
                        base = float(input("Base: "))

                        while True:
                            n_lados = float(input("Numero de lados: "))
                            
                            if n_lados == 3:
                                altura_base = float(input("Digite o valor da altura da base: "))
                                piramide = Piramide(altura, base, n_lados, altura_base)
                                triangulo1 = Triangle(base, altura_base, 0, 0, 0)
                                area_base = triangulo1.area_calculator()
                            
                            elif n_lados == 4:
                                piramide = Piramide(altura, base, n_lados, 0)
                                quadrado1 = Square(base)
                                area_base = quadrado1.area_calculator()
                                
                            elif n_lados == 5:
                                piramide = Piramide(altura, base, n_lados, 0)
                                hexagono1 = Hexagon(base)
                                area_base = hexagono1.area_calculator()
                                
                            elif n_lados == 6:
                                piramide = Piramide(altura, base, n_lados, 0)
                                pentagono1 = Pentagon(base)   
                                area_base = pentagono1.area_calculator() 
                            
                            else:
                                print("Valor incorreto!")
                                break
                        
                            while True:   
                                print("Escolha entre as opcoes a seguir: ")
                                print("|1|. Area da Base")
                                print("|2|. Area Lateral")
                                print("|3|. Area Total")
                                print("|4|. Volume")
                                print("|5|. Voltar")
                                
                                option3_6 = input()
                                
                                if option3_6 == "1":
                                    print(f"A area da base da piramide e: {area_base}")
                                elif option3_6 == "2":
                                    print(f"A area lateral da piramide e: {piramide.area_lateral()}")
                                elif option3_6 == "3":
                                    print(f"A area total da piramide e: {piramide.area_total()}")
                                elif option3_6 == "4":
                                    print(f"O volume da piramide e: {piramide.volume()}")
                                elif option3_6 == "5":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                                    
                                    
                            break
                        break
                    
                elif option3 == "7":
                    break
                
                else:
                    print("Valor incorreto!")
                                                
        elif option == "4":
            break
        
        else:
            print("Valor incorreto!")
        
if __name__ == "__main__":
    main()