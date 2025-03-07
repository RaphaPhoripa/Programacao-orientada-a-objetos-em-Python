class Aluno():
    # Método construtor que inicializa os atributos da classe Aluno
    def __init__(self, nome, idade, matricula):
        self.__nome = nome          # Atributo privado para armazenar o nome do aluno
        self.__idade = idade        # Atributo privado para armazenar a idade do aluno
        self.__matricula = matricula  # Atributo privado para armazenar a matrícula do aluno

    # Método getter para obter o nome do aluno
    @property
    def nome(self):
        return self.__nome

    # Método setter para modificar o nome do aluno
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    # Método para exibir os dados do aluno
    def mostra_dados(self):
        print("\n\nDados do aluno:")
        print("Nome: ", self.__nome)
        print("Idade: ", self.__idade)
        print("Matrícula: ", self.__matricula)

    # Método que incrementa a idade do aluno em 1 (simulando um aniversário)
    def faz_aniversario(self):
        self.__idade = self.__idade + 1

# Criando um objeto da classe Aluno com os valores iniciais
aluno1 = Aluno("João", 23, 1234)

# Exibindo os dados iniciais do aluno
aluno1.mostra_dados()

# Chamando o método faz_aniversario() para aumentar a idade do aluno em 1
aluno1.faz_aniversario()

# Exibindo novamente os dados do aluno para verificar se a idade foi atualizada
aluno1.mostra_dados()

# Testando os métodos getter e setter da classe
print("\n\n")
print(aluno1.nome)  # Obtendo o nome do aluno usando o getter
aluno1.nome = "João da Silva"  # Alterando o nome do aluno usando o setter
print(aluno1.nome)  # Exibindo o novo nome para confirmar a alteração