print('Hello Python')

# Declarar uma Classe em Python

class Carro:
    def __init__(self, modelo: str, cor: str, placa: str):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.velocidade = 0

    def buzinar(self):
        print('carro', self.modelo, 'buzinou')

    def acelerar(self):
            self.velocidade += 10

    def frear(self):
        self.velocidade += 10
        if self.velocidade < 0:
            self.velocidade = 0

# Instanciar uma classe em Python:  

def main():
    carro1 = Carro('Gol', 'Vermelho', 'ABC-1234')
    carro2 = Carro('Fox', 'Prata', 'XYZ-1234')
    
    carro1.buzinar()
    carro2.acelerar()
    print('Velocidade do', carro2.modelo, ':', carro2.velocidade, 'km/h')
    
main()
    
'''main()
carro Gol buzinou
velocidade do Fox : 10 km/h
Note como o parâmetro self não é utilizado na chamada do método. Note também a diferença entre acessar
métodos e atributos do objeto carro2: para acessar os métodos utiliza-se parênteses, diferentemente do
acesso aos atributos.'''    
    
# 

