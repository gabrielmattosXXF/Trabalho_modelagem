from tkinter import Tk, Label, Entry, Button, StringVar, Toplevel
from Ficha import Ficha

class view_editar_ficha:
    def __init__(self):
        self.root = Tk()
        self.root.title("Criar Ficha")

        self.root.geometry("500x400")  # Ajuste o tamanho conforme necessário
        self.root.configure(bg="#F0F0F0")  # Cor de fundo

        self.label_nome_ficha = Label(self.root, text="Nome da Ficha:", font=("Arial", 12))
        self.entry_nome_ficha = Entry(self.root, font=("Arial", 12))
        self.label_nome_ficha.grid(row=0, column=0, pady=10)
        self.entry_nome_ficha.grid(row=0, column=1, pady=10)

        self.exercicios = []
        self.add_exercicio_button = Button(self.root, text="Adicionar Exercício", command=self.adicionar_exercicio, font=("Arial", 12))
        self.add_exercicio_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.registrar_ficha_button = Button(self.root, text="Registrar Ficha", command=self.registrar_ficha, font=("Arial", 12))
        self.registrar_ficha_button.grid(row=2, column=0, columnspan=2, pady=10)

    def adicionar_exercicio(self):
        exercicio = {}
        root_exercicio = Toplevel(self.root)
        root_exercicio.title("Adicionar Exercício")

        root_exercicio.geometry("400x300")  # Ajuste o tamanho conforme necessário
        root_exercicio.configure(bg="#F0F0F0")  # Cor de fundo

        label_nome = Label(root_exercicio, text="Nome do Exercício:", font=("Arial", 12))
        entry_nome = Entry(root_exercicio, font=("Arial", 12))
        label_nome.grid(row=0, column=0, pady=10)
        entry_nome.grid(row=0, column=1, pady=10)

        label_carga = Label(root_exercicio, text="Carga:", font=("Arial", 12))
        entry_carga = Entry(root_exercicio, font=("Arial", 12))
        label_carga.grid(row=1, column=0, pady=10)
        entry_carga.grid(row=1, column=1, pady=10)

        label_repeticoes = Label(root_exercicio, text="Repetições:", font=("Arial", 12))
        entry_repeticoes = Entry(root_exercicio, font=("Arial", 12))
        label_repeticoes.grid(row=2, column=0, pady=10)
        entry_repeticoes.grid(row=2, column=1, pady=10)

        label_series = Label(root_exercicio, text="Séries:", font=("Arial", 12))
        entry_series = Entry(root_exercicio, font=("Arial", 12))
        label_series.grid(row=3, column=0, pady=10)
        entry_series.grid(row=3, column=1, pady=10)

        confirmar_button = Button(root_exercicio, text="Confirmar", command=lambda: self.confirmar_exercicio(exercicio, root_exercicio), font=("Arial", 12))
        confirmar_button.grid(row=4, column=0, columnspan=2, pady=10)

        exercicio['nome'] = entry_nome
        exercicio['carga'] = entry_carga
        exercicio['repeticoes'] = entry_repeticoes
        exercicio['series'] = entry_series

    def confirmar_exercicio(self, exercicio, root_exercicio):
        self.exercicios.append(exercicio)
        root_exercicio.destroy()
        self.atualizar_exercicios()

    def registrar_ficha(self):
        nome_ficha = self.entry_nome_ficha.get()
        nova_ficha = Ficha(nome_ficha)

        for exercicio in self.exercicios:
            nome = exercicio['nome'].get()
            carga = exercicio['carga'].get()
            repeticoes = exercicio['repeticoes'].get()
            series = exercicio['series'].get()

            nova_ficha.adicionar_exercicio(nome, carga, repeticoes, series, comentario="")

        self.mostrar_exercicios_cadastrados()

    def mostrar_exercicios_cadastrados(self):
        if self.exercicios:
            lista_exercicios = "\n".join([f"{i + 1}. {exercicio['nome'].get()}" for i, exercicio in enumerate(self.exercicios)])
            mensagem = f"Exercícios Cadastrados:\n{lista_exercicios}"
            label_resultado = Label(self.root, text=mensagem, font=("Arial", 12), fg="green")
            label_resultado.grid(row=3, column=0, columnspan=2, pady=10)
        else:
            label_resultado = Label(self.root, text="Nenhum exercício cadastrado ainda.", font=("Arial", 12), fg="red")
            label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

    def run(self):
        self.root.mainloop()

view = view_editar_ficha()
view.run()