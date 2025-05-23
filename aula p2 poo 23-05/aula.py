# importando os framework
import tkinter as tk
from tkinter import messagebox

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # método abstrato
    def apresentar(self):
        raise NotImplementedError("Subclasse deve implementar o método apresentar().")
    
# 1ª subclass
class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    # implemnta o método apresentar
    def apresentar(self):
        return f"Sou o aluno {self.nome} e curso {self.curso}."

# 2ª subclass
class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

   # implementando o método apresentar
    def apresentar(self):
      return f"Sou o professor {self.nome} e leciono {self.disciplina}."
    
# função polifórmica
def apresentar_pessoa(pessoa: Pessoa):
    return pessoa.apresentar()

# class cria a interface gráfica
class SistemaApresentacoes:
    def __init__(self, pessoas):
        # recebe uma lista de objetos de aluno e professor
        self.pessoas = pessoas
        # criar a interface gráfica
        self.janela = tk.Tk()
        # o título da minha janela ou root
        self.janela.title("Sistema de Apresentações")
        # o tamanho e posição da janela
        self.janela.geometry("300x150")
        # crie um botão
        self.botao = tk.Button(self.janela, text="Mostrar Apresentações", command=self.apresentar_pessoas)
        self.botao.pack(pady=40)

    # criando um método que absorve o método polifórmico
    def apresentar_pessoas(self):
        mensagens = [apresentar_pessoa(p) for p in self.pessoas]

        messagebox.showinfo("Apresentações", "\n".join(mensagens))

    def iniciar(self):
        self.janela.mainloop()

aluno = Aluno("Zé da Manga", "Engenharia de Software")
professor = Professor("Zé da Couve", "POO")
pessoas = [aluno, professor]

sistema = SistemaApresentacoes(pessoas)
sistema.iniciar()