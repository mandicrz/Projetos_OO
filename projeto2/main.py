from package.maths_bidimensional import *
from package.maths_tridimensional import *

def main():
    while True: 
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
                print("|3|. Voltar")
                    
                option1 = input()
                
                if option1 == "1":
                    while True:
                        print("Você escolheu criar um ponto! Digite suas coordenadas (separadas por vírgula): ")

                        coordenadas = input("Ponto: ").split(",")
                        x = float(coordenadas[0])
                        y = float(coordenadas[1])

                        ponto1 = Point(x, y)

                        print(f"O ponto criado foi: ({ponto1.x}, {ponto1.y})")
                        
                        while True:
                            print("Escolha entre as opções a seguir:")
                            print("|1|. Distância da Origem")
                            print("|2|. Criar outro ponto")
                            print("|3|. Voltar")
                            
                            option1_1 = input()
                            
                            if option1_1 == "1":
                                print(f"A distância do ponto ({ponto1.x}, {ponto1.y}) até a origem é: {ponto1.distance_point_origin()}")
                                
                            elif option1_1 == "2":
                                print("Digite as coordenadas do outro ponto: ")
                                coordenadas2 = input("Ponto 2: ").split(",")
                                x2 = float(coordenadas2[0])
                                y2 = float(coordenadas2[1])
                                    
                                ponto2 = Point(x2, y2)
                                    
                                print(f"O segundo ponto criado foi: ({ponto2.x}, {ponto2.y}), e sua distância do primeiro ponto ({ponto1.x}, {ponto1.y}) é: {ponto1.distance_points(ponto2)}")
                                
                            
                            elif option1_1 == "3":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                    
                        
                
                elif option1 == "2":
                    while True:
                        print("Você escolheu criar um segmento de reta! Digite o primeiro ponto (x e y separados por vírgula): ")
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
                            print("Escolha entre as opções a seguir: ")                
                            print("|1|. Distância de um ponto qualquer ao segmento")
                            print("|2|. Verificar se um ponto qualquer está perto do segmento")
                            print("|3|. Ponto médio do segmento")
                            print("|4|. Voltar")

                            option1_2 = input()
                            
                            if option1_2 == "1":
                                print("Digite o ponto que quer comparar: ")
                                coordenadas3 = input("Ponto: ").split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                print(f"O ponto ({ponto3.x}, {ponto3.y}) está a uma distância de {segmento.distance_point_segment_calculator(ponto3)}")
                                                    
                            
                            elif option1_2 == "2":
                                print("Digite um ponto que quer verificar: ")
                                coordenadas3 = input("Ponto: ").split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                if segmento.close_point(ponto3):
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) está perto do segmento!")
                                    
                                else:
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) não está perto do segmento!")
                                
                            
                            elif option1_2 == "3":
                                print(f"O ponto médio do segmento é: {segmento.mid_point()}")
                                
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
                print("|1|. Círculo")
                print("|2|. Hexágono")
                print("|3|. Pentágono")
                print("|4|. Retângulo")
                print("|5|. Quadrado")
                print("|6|. Triângulo")
                print("|7|. Voltar")
                
                option2 = input()
                
                if option2 == "1":
                    while True:
                        print("Você escolheu criar um círculo! Digite o raio e o centro (x e y separados por vírgula) do mesmo (separados por enter):")
                        
                        raio = float(input("Raio: "))
                        circle = input("Centro: ").split(",")
                        x = float(circle[0])
                        y = float(circle[1])
                        
                        centro = Point(x, y)
                        circulo = Circle(raio, centro)
                        
                        while True: 
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Diâmetro")
                            print("|2|. Área")
                            print("|3|. Perímetro")
                            print("|4|. Verificar se um ponto qualquer está dentro do círculo")
                            print("|5|. Voltar")
                            
                            option2_1 = input()
                            
                            if option2_1 == "1":
                                print(f"O diâmetro do círculo de raio {raio} é: {circulo.diameter_calculator()}")
                                
                                
                            elif option2_1 == "2":
                                print(f"A área do círculo de raio {raio} é: {circulo.area_calculator()}")
                                
                                
                            elif option2_1 == "3":
                                print(f"O perímetro do círculo de raio {raio} é: {circulo.perimeter_calculator()}")
                                
                            elif option2_1 == "4":
                                print("Digite o ponto que quer verificar (x e y separados por vírgula): ")
                                ponto = input("Ponto: ").split(",")
                                x2 = float(ponto[0])
                                y2 = float(ponto[1])
                                    
                                ponto = Point(x2, y2)
                                    
                                if circulo.inside_point(ponto):
                                    print(f"O ponto ({ponto.x}, {ponto.y}) está dentro do círculo")
                                else:
                                    print(f"O ponto ({ponto.x}, {ponto.y}) não está dentro do círculo")
                                
                            elif option2_1 == "5":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                    
                elif option2 == "2": 
                    while True:
                        print("Você escolheu criar um hexágono! Digite a medida de seu lado: ")
                        hexagono = Hexagon(float(input("Lado: ")))

                        while True:
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Área")
                            print("|2|. Perímetro")
                            print("|3|. Soma dos ângulos internos")
                            print("|4|. Voltar")
                            
                            option2_2 = input()
                            
                            if option2_2 == "1":
                                print(f"A área do hexágono é: {hexagono.area_calculator()}")

                            elif option2_2 == "2":
                                print(f"O perímetro do hexágono é: {hexagono.perimeter_calculator()}")
                            
                            elif option2_2 == "3":
                                print(f"A soma dos ângulos internos do hexágono é: {hexagono.sum_intern_angles(6)}°")
                                
                            elif option2_2 == "4":
                                break
                            
                            else:
                                print("Valor incorreto!")
                                
                        break
                
                elif option2 == "3":
                    while True:
                        print("Você escolheu criar um pentágono! Digite a medida de seu lado: ")
                        pentagono = Pentagon(float(input("Lado: ")))   
                        
                        while True: 
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Área")
                            print("|2|. Perímetro")
                            print("|3|. Soma dos ângulos internos")
                            print("|4|. Voltar")
                            
                            option2_3 = input()
                            
                            if option2_3 == "1":
                                print(f"A área do pentágono é: {pentagono.area_calculator()}")

                            elif option2_3 == "2":
                                print(f"O perímetro do pentágono é: {pentagono.perimeter_calculator()}")
                            
                            elif option2_3 == "3":
                                print(f"A soma dos ângulos internos do pentágono é: {pentagono.sum_intern_angles(5)}°")
                                
                            elif option2_3 == "4":
                                break
                            
                            else: 
                                print("Valor incorreto!")
                                                            
                        break
                    
                elif option2 == "4":
                    while True: 
                        print("Você escolheu criar um retângulo! Digite sua base e altura (seguidos por enter): ")
                        base = float(input("Base: "))
                        altura = float(input("Altura: "))
                        retangulo = Rectangle(base, altura)
                        
                        while True: 
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Área")
                            print("|2|. Perímetro")
                            print("|3|. Diagonal")
                            print("|4|. Soma dos ângulos internos")
                            print("|5|. Voltar")
                            
                            option2_4 = input()
                            
                            if option2_4 == "1":
                                print(f"A área do retângulo é: {retangulo.area_calculator()}")

                            elif option2_4 == "2":
                                print(f"O perímetro do retângulo é: {retangulo.perimeter_calculator()}")
                            
                            elif option2_4 == "3": 
                                print(f"A diagonal do retângulo é: {retangulo.diagonal_calculator()}")
                                
                            elif option2_4 == "4":
                                print(f"A soma dos ângulos internos do retângulo é: {retangulo.sum_intern_angles(4)}°")
                                
                            elif option2_4 == "5":
                                break     
                            
                            else: 
                                print("Valor incorreto!")     
                               
                        break
                elif option2 == "5":
                    while True: 
                        print("Você escolheu criar um quadrado! Digite a medida de seu lado: ")
                        quadrado = Square(float(input("Lado: ")))   
                        
                        while True: 
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Área")
                            print("|2|. Perímetro")
                            print("|3|. Diagonal")
                            print("|4|. Soma dos ângulos internos")
                            print("|5|. Voltar")
                            
                            option2_5 = input()
                            
                            if option2_5 == "1":
                                print(f"A área do quadrado é: {quadrado.area_calculator()}")

                            elif option2_5 == "2":
                                print(f"O perímetro do quadrado é: {quadrado.perimeter_calculator()}")
                            
                            elif option2_5 == "3": 
                                print(f"A diagonal do quadrado é: {quadrado.diagonal_calculator()}")
                                
                            elif option2_5 == "4":
                                print(f"A soma dos ângulos internos do quadrado é: {quadrado.sum_intern_angles(4)}°")
                                
                            elif option2_5 == "5":
                                break 
                            
                            else: 
                                print("Valor incorreto!")
                                         
                        break
                    
                elif option2 == "6":
                    while True: 
                        print("Você escolheu criar um triângulo! Digite a sua base e sua altura (separados por enter): ")
                        base = float(input("Base: "))
                        altura = float(input("Altura: "))
                        
                        print("Digite agora a medida de seus lados (separados por enter): ")
                        a = float(input("Lado A: "))
                        b = float(input("Lado B: "))
                        c = float(input("Lado C: "))
                        
                        triangulo = Triangle(base, altura, a, b, c)  
                        
                        if triangulo.triangle_exists(): 
                            while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área")
                                print("|2|. Perímetro")
                                print("|3|. Soma dos ângulos internos")
                                print("|4|. Tipo de triângulo com base em seus lados")
                                print("|5|. Voltar")
                                
                                option2_6 = input()

                                if option2_6 == "1":
                                    print(f"A área do triângulo é: {triangulo.area_calculator()}")

                                elif option2_6 == "2":
                                    print(f"O perímetro do triângulo é: {triangulo.perimeter_calculator()}")
                                    
                                elif option2_6 == "3":
                                    print(f"A soma dos ângulos internos do triângulo é: {triangulo.sum_intern_angles(3)}°")
                                    
                                elif option2_6 == "4":
                                    print(triangulo.type_of_triangle())
                                    
                                elif option2_6 == "5":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                                    
                            break
                        else:
                            print("O triângulo informado não atende aos requisitos de criação. Digite novos valores: ")
                
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
                print("|5|. Paralelepípedo")
                print("|6|. Pirâmide")
                print("|7|. Voltar")
                
                option3 = input()
                
                if option3 == "1":
                    while True:
                        print("Você escolheu criar um cilindro! Digite a sua raio e sua altura (separados por enter): ")
                        
                        raio = float(input("Raio: "))
                        altura = float(input("Altura: "))
                        
                        cilindro = Cilindro(raio, altura)
                        
                        while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área da Base")
                                print("|2|. Área Lateral")
                                print("|3|. Área Total")
                                print("|4|. Volume")
                                print("|5|. Perímetro")
                                print("|6|. Voltar")
                                
                                option3_1 = input()
                                
                                if option3_1 == "1":
                                    print(f"A área da base do cilindro é: {cilindro.area_base()}")
                                    
                                elif option3_1 == "2":
                                    print(f"A área lateral do cilindro é: {cilindro.area_lateral()}")
                                    
                                elif option3_1 == "3":
                                    print(f"A área total do cilindro é: {cilindro.area_total()}")  
                                    
                                elif option3_1 == "4":
                                    print(f"O volume do cilindro é: {cilindro.volume()}")
                                     
                                elif option3_1 == "5":
                                    print(f"O perímetro do cilindro é: {cilindro.perimetro()}")
                                    
                                elif option3_1 == "6":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                        break 
                        
                elif option3 == "2": 
                    while True:
                        print("Você escolheu criar um cone! Digite a sua raio e sua altura (separados por enter): ")
                        
                        raio = float(input("Raio: "))
                        altura = float(input("Altura: "))
                        
                        cone = Cone(raio, altura)
                        
                        while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área da Base")
                                print("|2|. Área Lateral")
                                print("|3|. Área Total")
                                print("|4|. Volume")
                                print("|5|. Perímetro")
                                print("|6|. Voltar")
                                
                                option3_2 = input()
                                
                                if option3_2 == "1":
                                    print(f"A área da base do cone é: {cone.area_base()}")
                                    
                                elif option3_2 == "2":
                                    print(f"A área lateral do cone é: {cone.area_lateral()}")
                                    
                                elif option3_2 == "3":
                                    print(f"A área total do cone é: {cone.area_total()}") 
                                        
                                elif option3_2 == "4":
                                    print(f"O volume do cone é: {cone.volume()}") 
                                    
                                elif option3_2 == "5":
                                    print(f"O perímetro do cone é: {cone.perimetro()}")
                                    
                                elif option3_2 == "6":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                        break 
        
                elif option3 == "3":
                    while True:
                        print("Você escolheu criar um cubo! Digite a medida da aresta: ")
                        
                        cubo = Cubo(float(input("Aresta: ")))
                        
                        while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área da Base")
                                print("|2|. Área Lateral")
                                print("|3|. Área Total")
                                print("|4|. Volume")
                                print("|5|. Diagonal Espacial")
                                print("|6|. Voltar")
                                
                                option3_3 = input()
                                
                                if option3_3 == "1":
                                    print(f"A área da base do cubo é: {cubo.area_base()}")
                                    
                                elif option3_3 == "2":
                                    print(f"A área lateral do cubo é: {cubo.area_lateral()}")
                                    
                                elif option3_3 == "3":
                                    print(f"A área total do cubo é: {cubo.area_total()}") 
                                     
                                elif option3_3 == "4":
                                    print(f"O volume do cubo é: {cubo.volume()}") 
                                    
                                elif option3_3 == "5":
                                    print(f"A diagonal espacial do cubo é: {cubo.diagonal_interna()}")
                                    
                                elif option3_3 == "6":
                                    break
                                
                                else: 
                                    print("Valor incorreto!")
                        break 
                    
                elif option3 == "4":
                    while True: 
                        print("Você escolheu criar uma esfera! Digite o raio da mesma: ")
                        
                        esfera = Esfera(float(input("Raio: ")))
                        
                        while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área Total")
                                print("|2|. Volume")
                                print("|3|. Perímetro")
                                print("|4|. Diâmetro")
                                print("|5|. Voltar")
                                
                                option3_4 = input()
                                
                                if option3_4 == "1":
                                    print(f"A área total da esfera é: {esfera.area_total()}")
                                    
                                elif option3_4 == "2":
                                    print(f"O volume da esfera é: {esfera.volume()}")
                                    
                                elif option3_4 == "3":
                                    print(f"O perímetro da esfera é: {esfera.perimetro()}") 
                                     
                                elif option3_4 == "4":
                                    print(f"O diâmetro da esfera é: {esfera.diametro()}")
                                    
                                elif option3_4 == "5":
                                    break
                                
                                else:
                                    print("Valor incorreto!")
                                    
                        break 
                
                elif option3 == "5":
                    while True: 
                        print("Você escolheu criar um paralelepípedo! Digite a medida da largura, comprimento e altura (separadas por enter): ")
                        
                        largura = float(input("Largura: "))
                        comprimento = float(input("Comprimento: "))
                        altura = float(input("Altura: "))
                        
                        paralelepipedo = Paralelepipedo(largura, comprimento, altura)
                        
                        while True: 
                                print("Escolha entre as opções a seguir: ")
                                print("|1|. Área da Base")
                                print("|2|. Área Lateral")
                                print("|3|. Área Total")
                                print("|4|. Volume")
                                print("|5|. Diagonal Espacial")
                                print("|6|. Voltar")
                                
                                option3_5 = input()
                                
                                if option3_5 == "1":
                                    print(f"A área da base do paralelepípedo é: {paralelepipedo.area_base()}")
                                    
                                elif option3_5 == "2":
                                    print(f"A área lateral do paralelepípedo é: {paralelepipedo.area_lateral()}")
                                    
                                elif option3_5 == "3":
                                    print(f"A área total do paralelepípedo é: {paralelepipedo.area_total()}") 
                                     
                                elif option3_5 == "4":
                                    print(f"O volume do paralelepípedo é: {paralelepipedo.volume()}")
                                    
                                elif option3_5 == "5":
                                    print(f"A diagonal espacial do paralelepípedo é: {paralelepipedo.diagonal_interna()}")
                                    
                                elif option3_5 == "6":
                                    break
                                
                                else: 
                                    print("Valor incorreto!")
                                    
                        break 
                
                elif option3 == "6":
                    while True:
                        print("Você escolheu criar uma pirâmide, digite as medidas da altura e da base e o número de lados da mesma (separadas por enter):")
                        
                        altura = float(input("Altura: "))
                        base = float(input("Base: "))
                        n_lados = float(input("Número de lados: "))
                        
                        
                        print("Escolha a base de acordo com a pirâmide que deseja criar: ")
                        print("|1|. Triangular")
                        print("|2|. Quadrangular")
                        print("|3|. Pentagonal")
                        print("|4|. Hexagonal")
                        
                        tipo_base = float(input("Tipo da base: "))
                        
                        if tipo_base == 1:
                            altura_base = float(input("Digite o valor da altura da base: "))
                            piramide = Piramide(altura, base, n_lados, tipo_base, altura_base)
                            triangulo1 = Triangle(base, altura_base, 0, 0, 0)
                            area_base = triangulo1.area_calculator()
                        
                        elif tipo_base == 2:
                            piramide = Piramide(altura, base, n_lados, tipo_base, 0)
                            quadrado1 = Square(base)
                            area_base = quadrado1.area_calculator()
                            
                        elif tipo_base == 3:
                            piramide = Piramide(altura, base, n_lados, tipo_base, 0)
                            hexagono1 = Hexagon(base)
                            area_base = hexagono1.area_calculator()
                            
                        elif tipo_base == 4:
                            piramide = Piramide(altura, base, n_lados, tipo_base, 0)
                            pentagono1 = Pentagon(base)   
                            area_base = pentagono1.area_calculator() 
                        
                        else:
                            print("Valor incorreto!")
                          
                        while True:   
                            print("Escolha entre as opções a seguir: ")
                            print("|1|. Área da Base")
                            print("|2|. Área Lateral")
                            print("|3|. Área Total")
                            print("|4|. Volume")
                            print("|5|. Voltar")
                            
                            option3_6 = input()
                            
                            if option3_6 == "1":
                                print(f"A área da base da pirâmide é: {area_base}")
                            elif option3_6 == "2":
                                print(f"A área lateral da pirâmide é: {piramide.area_lateral()}")
                            elif option3_6 == "3":
                                print(f"A área total da pirâmide é: {piramide.area_total()}")
                            elif option3_6 == "4":
                                print(f"O volume da pirâmide é: {piramide.volume()}")
                            elif option3_6 == "5":
                                break
                            
                            else:
                                print("Valor incorreto!")
                           
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