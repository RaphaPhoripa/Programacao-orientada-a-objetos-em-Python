import math

class FormaGeometrica:
    def calcular_area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado: float):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

def main():
    tipo = input("Digite a forma geométrica (quadrado, retangulo, circulo): ").strip().lower()
    
    if tipo == "quadrado":
        lado = float(input("Digite o lado do quadrado: "))
        forma = Quadrado(lado)
    elif tipo == "retangulo":
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        forma = Retangulo(base, altura)
    elif tipo == "circulo":
        raio = float(input("Digite o raio do círculo: "))
        forma = Circulo(raio)
    else:
        print("Forma geométrica inválida!")
        return
    
    print(f"A área da forma escolhida é: {forma.calcular_area():.2f}")
    
main()
0,
