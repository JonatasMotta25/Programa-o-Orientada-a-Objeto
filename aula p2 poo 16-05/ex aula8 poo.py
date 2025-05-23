# Classe Pessoa - Representa uma pessoa genérica
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Nome da pessoa
        self.idade = idade  # Idade da pessoa

    def apresentar(self):
        # Método que retorna as informações básicas sobre a pessoa
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Classe Aluno - Representa um aluno, que é um tipo específico de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)  # Inicializa os atributos da classe Pessoa
        self.matricula = matricula  # Matrícula do aluno
        self.curso = curso  # Curso que o aluno está fazendo
        self.nota = 0  # Inicializa a nota do aluno como 0

    def apresentar(self):
        # Retorna as informações do aluno, incluindo matrícula e curso
        return f"{super().apresentar()}, Matrícula: {self.matricula}, Curso: {self.curso}"

    def atribuir_nota(self, nota):
        # Soma a nota atual com a nova nota (caso já tenha sido atribuída uma nota antes)
        self.nota += nota
        return f"A nota do aluno {self.nome} agora é {self.nota}"

# Classe Professor - Representa um professor, que também é uma pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, departamento):
        super().__init__(nome, idade)  # Inicializa os atributos da classe Pessoa
        self.disciplina = disciplina  # Disciplina que o professor ensina
        self.departamento = departamento  # Departamento onde o professor trabalha

    def apresentar(self):
        # Retorna as informações do professor, incluindo disciplina e departamento
        return f"{super().apresentar()}, Disciplina: {self.disciplina}, Departamento: {self.departamento}"

    def conversar(self, aluno):
        # Simula uma conversa entre o professor e um aluno
        return f"O professor {self.nome} está conversando com o aluno {aluno.nome}."

    def gerar_nota(self, aluno, nota):
        # O professor atribui ou soma uma nota para o aluno
        aluno.atribuir_nota(nota)
        return f"A nota do aluno {aluno.nome} foi atualizada para {aluno.nota}"

# Classe Apresentar - Serve para mostrar as informações de qualquer pessoa
class Apresentar:
    @staticmethod
    def mostrar(pessoas):
        # Para cada pessoa na lista, chama o método 'apresentar' e exibe as informações
        for pessoa in pessoas:
            print(pessoa.apresentar())

# Criando instâncias para testar as classes
aluno1 = Aluno("Carlos", 20, "12345", "Engenharia")  # Criando um aluno
professor1 = Professor("Dr. Silva", 40, "Matemática", "Exatas")  # Criando um professor

# Exibindo as informações iniciais
print("Apresentando Aluno e Professor:")
Apresentar.mostrar([aluno1, professor1])  # Mostra o nome e os detalhes de cada pessoa

# Realizando algumas interações
print("\nProfessor conversando com o aluno:")
print(professor1.conversar(aluno1))  # O professor conversa com o aluno

print("\nAtribuindo e atualizando nota do aluno:")
print(professor1.gerar_nota(aluno1, 8))  # O professor atribui a primeira nota (8)
print(professor1.gerar_nota(aluno1, 7))  # O professor soma a nota (7), totalizando 15

# Exibindo novamente as informações após a interação
print("\nApresentando Aluno e Professor após a atualização da nota:")
Apresentar.mostrar([aluno1, professor1])  # Mostra novamente as informações com a nota atualizada
