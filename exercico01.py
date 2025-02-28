class Aluno:
    def __init__(self, nome: str, idade: int, matricula: int):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
    
    def mostra_dados(self):
        print(f"Nome: {self.__nome}\nIdade: {self.__idade}\nMatrícula: {self.__matricula}")
    
    def faz_aniversario(self):
        self.__idade += 1
        print("Feliz aniversário! Sua nova idade é:", self.__idade)
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome
        
def main():
    aluno1 = Aluno("João", 20, 12345)
    
    print("Dados iniciais do aluno:")
    aluno1.mostra_dados()
    
    aluno1.faz_aniversario()
    
    print("Dados após aniversário:")
    aluno1.mostra_dados()
    
    print("Nome atual do aluno:", aluno1.nome)
    aluno1.nome = "Carlos"
    print("Nome atualizado do aluno:", aluno1.nome)
    
main()
