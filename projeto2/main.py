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
                        print("Você escolheu criar um ponto! Digite suas coordenadas separadas por vírgula: ")

                        coordenadas = input().split(",")
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
                                coordenadas2 = input().split(",")
                                x2 = float(coordenadas2[0])
                                y2 = float(coordenadas2[1])
                                    
                                ponto2 = Point(x2, y2)
                                    
                                print(f"O segundo ponto criado foi: ({ponto2.x}, {ponto2.y}), e sua distância do primeiro ponto ({ponto1.x}, {ponto1.y}) é: {ponto1.distance_points(ponto2)}")
                                
                            
                            elif option1_1 == "3":
                                break
                        break
                    
                        
                
                elif option1 == "2":
                    while True:
                        print("Você escolheu criar um segmento de reta! Digite o primeiro ponto: ")
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
                        while True: 
                            print("Escolha entre as opções a seguir: ")                
                            print("|1|. Distância de um ponto qualquer ao segmento")
                            print("|2|. Verificar se um ponto qualquer está perto do segmento")
                            print("|3|. Ponto médio do segmento")
                            print("|4|. Voltar")

                            option1_2 = input()
                            
                            if option1_2 == "1":
                                print("Digite o ponto que quer comparar: ")
                                coordenadas3 = input().split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                print(f"O ponto ({ponto3.x}, {ponto3.y}) está a uma distância de {segmento.distance_point_segment_calculator(ponto3)}")
                                                    
                            
                            elif option1_2 == "2":
                                print("Digite um ponto que quer verificar: ")
                                coordenadas3 = input().split(",")
                                x3 = float(coordenadas3[0])
                                y3 = float(coordenadas3[1])
                                ponto3 = Point(x3, y3)
                                
                                if segmento.close_point(ponto3):
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) está perto do segmento!)")
                                    
                                else:
                                    print(f"O ponto ({ponto3.x}, {ponto3.y}) não está perto do segmento!")
                                
                            
                            elif option1_2 == "3":
                                print(f"O ponto médio do segmento é: {segmento.mid_point()}")
                                
                            elif option1_2 == "4":
                                break
                        break
                            
                elif option1 == "3":
                    break

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
                        print("Você escolheu criar um círculo! Digite o raio e o centro do mesmo: (separados por enter)")
                        
                        raio = input()
                        circle = input().split(",")
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
                                break
                                
                                
                            if option2_1 == "2":
                                print(f"A área do círculo de raio {raio} é: {circulo.area_calculator()}")
                                break
                                
                                
                            if option2_1 == "3":
                                print(f"O perímetro do círculo de raio {raio} é: {circulo.perimeter_calculator()}")
                                break
                                
                                
                            if option2_1 == "4":
                                print("Digite o ponto que quer verificar: ")
                                ponto = input().split(",")
                                x2 = float(ponto[0])
                                y2 = float(ponto[1])
                                    
                                ponto = Point(x2, y2)
                                    
                                if circulo.inside_point(ponto):
                                    print(f"O ponto ({ponto.x}, {ponto.y}) está dentro do círculo")
                                else:
                                    print(f"O ponto ({ponto.x}, {ponto.y}) não está dentro do círculo")
                                
                            if option2_1 == "5":
                                break
                        break
                    
                elif option2 == "2": 
                    while True:
                        print("Você escolheu criar um hexágono! Digite a medida de seu lado: ")
                        hexagono = Hexagon(float(input()))

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
                        break
                
                elif option2 == "3":
                    while True:
                        print("Você escolheu criar um pentágono! Digite a medida de seu lado: ")
                        pentagono = Pentagon(float(input()))   
                        
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
                        break
                elif option2 == "4":
                    while True: 
                        print("Você escolheu criar um retângulo! Digite sua base e altura: ")
                        base = float(input())
                        altura = float(input())
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
                               
                        break
                elif option2 == "5":
                    while True: 
                        print("Você escolheu criar um quadrado! Digite a medida de seu lado: ")
                        quadrado = Square(float(input()))   
                        
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
                        break
                    
                elif option2 == "6":
                    while True: 
                        print("Você escolheu criar um triângulo! Digite a sua base e sua altura (separados por enter): ")
                        base = float(input())
                        altura = float(input())
                        
                        print("Digite agora a medida de seus lados (separados por enter): ")
                        a = float(input())
                        b = float(input())
                        c = float(input())
                        
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
                            break
                        else:
                            print("O triângulo informado não atende aos requisitos de criação. Digite novos valores: ")
                
                elif option2 == "7":
                    break                 
                        
        elif option == "4":
            break
        
if __name__ == "__main__":
    main()