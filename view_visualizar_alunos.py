import tkinter as tk
from tkinter import ttk
from Usuario import Personal, Aluno
from Treino import Treino
from Ficha import Ficha

class view_visualizar_alunos:
    def __init__(self, personal):
        self.personal = personal
        self.root = tk.Toplevel()
        self.root.title("Visualizar Alunos")

        self.tree = ttk.Treeview(self.root, columns=('Nome', 'Email', 'Idade', 'Telefone'))
        self.tree.heading('#0', text='Nome')
        self.tree.heading('#1', text='Email')
        self.tree.heading('#2', text='Idade')
        self.tree.heading('#3', text='Telefone')
        self.tree.pack(expand=True, fill='both')

        self.atualizar_tabela()

        self.tree.bind('<Double-1>', self.mostrar_detalhes_aluno)

    def atualizar_tabela(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for aluno_nome, aluno_obj in self.personal.alunos.items():
            self.tree.insert('', 'end', text=aluno_nome, values=(aluno_obj.get_email(), aluno_obj.get_idade(), aluno_obj.get_telefone()))

    def mostrar_detalhes_aluno(self, event):
        item = self.tree.selection()[0] 
        aluno_nome = self.tree.item(item, 'text')
        aluno_obj = self.personal.alunos[aluno_nome]

        DetalhesAlunoView(aluno_obj)

class DetalhesAlunoView:
    def __init__(self, aluno):
        self.aluno = aluno
        self.root = tk.Toplevel()
        self.root.title(f"Detalhes do Aluno - {aluno.get_nome()}")

        label_nome = tk.Label(self.root, text=f"Nome: {aluno.get_nome()}")
        label_nome.pack()

        label_email = tk.Label(self.root, text=f"Email: {aluno.get_email()}")
        label_email.pack()

        label_idade = tk.Label(self.root, text=f"Idade: {aluno.get_idade()}")
        label_idade.pack()

        label_telefone = tk.Label(self.root, text=f"Telefone: {aluno.get_telefone()}")
        label_telefone.pack()

        label_CPF = tk.Label(self.root, text=f"CPF: {aluno.get_CPF()}")
        label_CPF.pack()

        label_treino = tk.Label(self.root, text=f"Data de Início do Treino: {aluno.treino.dataInicio}")
        label_treino.pack()

        label_personal = tk.Label(self.root, text=f"Personal: {aluno.Personal.get_nome()}")
        label_personal.pack()

treino_aluno1 = Treino("01/01/2023", "01/02/2023")
treino_aluno2 = Treino("01/01/2023", "01/02/2023")

exercicios_aluno1 = [("Supino", 50, 10, 3, "Comentário 1"), ("Rosca direta", 10, 10, 3, "Comentário 2")]
exercicios_aluno2 = [("Agachamento", 80, 12, 4, "Comentário 1"), ("Corrida", 0, 30, 5, "Comentário 2")]

treino_aluno1.criaFicha("Ficha 1", exercicios_aluno1)
treino_aluno2.criaFicha("Ficha 2", exercicios_aluno2)

personal1 = Personal("Personal 1", "personal1@email.com", "senha123", "123.456.789-01", 30, "123456789")
personal2 = Personal("Personal 2", "personal2@email.com", "456", "987.654.321-01", 25, "987654321")

aluno1 = Aluno("Aluno 1", "aluno1@email.com", "senha789", "111.222.333-01", 22, "111222333", personal1)
aluno2 = Aluno("Aluno 2", "aluno2@email.com", "senhaabc", "444.555.666-01", 28, "444555666", personal2)

aluno1.set_treino(treino_aluno1)
aluno2.set_treino(treino_aluno2)

personal1.vincularAluno(aluno1)
personal2.vincularAluno(aluno2)

view_personal1 = view_visualizar_alunos(personal1)
view_personal2 = view_visualizar_alunos(personal2)

view_personal1.root.mainloop()
view_personal2.root.mainloop()