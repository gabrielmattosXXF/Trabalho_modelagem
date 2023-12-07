from tkinter import Tk, Label, Entry, Button, Frame, StringVar, ttk, Canvas, Toplevel
from tkinter import Tk, Label, Button, Frame, StringVar, ttk, Text, Scrollbar, Canvas
import tkinter as tk
from Ficha import Ficha
from Exercicio import Exercicio

class view_criar_ficha:

    def __init__(self, fichas):
        self.i = 0
        self.fichas = fichas
        self.root = Tk()
        self.criar_ficha_entries = []
        self.exercicios = {}  # dicionário para armazenar as instâncias de view_criar_ficha
        self.screen()
        self.create_widgets()
        self.root.mainloop()
        print(self.i)

    def screen(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        # Configurações de Tamanho e Posição
        largura_janela = 500
        altura_janela = 600

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Criar treino")
        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(expand=True, fill="both", pady=20)

        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        canvas.configure(yscrollcommand=scrollbar.set)

        def on_scroll(*args):
            canvas.yview(*args)

        scrollbar.config(command=on_scroll)

        self.content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.content_frame, anchor=tk.NW)

        self.label_nome_ficha = Label(self.content_frame, text="Nome da Ficha:", font=("Arial", 12))
        self.entry_nome_ficha = Entry(self.content_frame, font=("Arial", 12))
        self.label_nome_ficha.grid(row=self.i, column=0, pady=10)
        self.entry_nome_ficha.grid(row=self.i, column=1, pady=10)
        self.i+=1

        self.add_exercicio_button = Button(self.content_frame, text="Adicionar Exercício", command=self.adicionar_exercicio, font=("Arial", 12))
        self.add_exercicio_button.grid(row=self.i, column=0, columnspan=2, pady=10)
        self.i+=1

        self.registrar_ficha_button = Button(self.content_frame, text="Registrar Ficha", command=self.registrar_ficha, font=("Arial", 12))
        self.registrar_ficha_button.grid(row=self.i, column=0, columnspan=2, pady=10)
        self.i+=1



        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        self.content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def adicionar_exercicio(self):
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

        label_coment = Label(root_exercicio, text="Comentário:", font=("Arial", 12))
        entry_coment = Entry(root_exercicio, font=("Arial", 12))
        label_coment.grid(row=4, column=0, pady=10)
        entry_coment.grid(row=4, column=1, pady=10)

        entradas = [entry_nome, entry_carga, entry_repeticoes, entry_series, entry_coment]

        confirmar_button = Button(root_exercicio, text="Confirmar", command=lambda: self.confirmar_exercicio(entradas, root_exercicio), font=("Arial", 12))
        confirmar_button.grid(row=5, column=0, columnspan=2, pady=10)

    def confirmar_exercicio(self, entradas, root_exercicio):
        exerc = Exercicio(entradas[0].get(), entradas[1].get(), entradas[2].get(), entradas[3].get(), entradas[4].get())
        self.exercicios[str(exerc.nome)] = exerc

        print(exerc.nome, exerc.carga, exerc.repeticoes, exerc.series, exerc.comentario)
        root_exercicio.destroy()

        Label(self.content_frame, text=exerc.nome, font=("Helvetica", 16), bg="#f0f0f0").grid(row=self.i, column=0, columnspan=2, pady=10)
        self.i += 1

        Label(self.content_frame, text="", height=1)

        labels_info = {"Carga:":"carga", "Repetições:":"repeticoes", "Séries:":"series"}
        for label_info, value in labels_info.items():
            Label(self.content_frame, text=label_info, font=("Helvetica", 12), bg="#f0f0f0").grid(row=self.i, column=0, pady=5)
            Label(self.content_frame, text=getattr(exerc, value), font=("Helvetica", 12), bg="#f0f0f0").grid(row=self.i, column=1, pady=5)
            self.i += 1

        Label(self.content_frame, text="Comentário:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=self.i, column=0, pady=5)
        text_comentario = Text(self.content_frame, height=4, width=30, font=("Helvetica", 12))
        text_comentario.grid(row=self.i, column=1, pady=5)
        text_comentario.insert("1.0", exerc.comentario)
        text_comentario.config(state="disabled")
        scrollbar_problemas = Scrollbar(self.content_frame, command=text_comentario.yview)
        scrollbar_problemas.grid(row=self.i, column=2, sticky="nsew")
        text_comentario.config(yscrollcommand=scrollbar_problemas.set)
        self.i += 1


        self.root.update_idletasks()

    def registrar_ficha(self):
        nome_ficha = self.entry_nome_ficha.get()
        nova_ficha = Ficha(nome_ficha)

        for exercicio in self.exercicios.values():

            nova_ficha.adicionar_exercicio(exercicio.nome, exercicio.carga, exercicio.repeticoes, exercicio.series, exercicio.comentario)

        # self.mostrar_exercicios_cadastrados()
        self.fichas.append(nova_ficha)

        self.root.destroy()
        # fazer a volta para a origem

    # def mostrar_exercicios_cadastrados(self):
    #     # if self.exercicios:
    #     #     lista_exercicios = "\n".join([f"{i + 1}. {exercicio['nome'].get()}" for i, exercicio in enumerate(self.exercicios)])
    #     #     mensagem = f"Exercícios Cadastrados:\n{lista_exercicios}"
    #     #     label_resultado = Label(self.root, text=mensagem, font=("Arial", 12), fg="green")
    #     #     label_resultado.grid(row=3, column=0, columnspan=2, pady=10)
    #     # else:
    #     #     label_resultado = Label(self.root, text="Nenhum exercício cadastrado ainda.", font=("Arial", 12), fg="red")
    #     #     label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

    #     print("Ficha criada com sucesso!")
    #     print("Exercícios cadastrados:")
    #     for exercicio in self.exercicios.values():
    #         print(exercicio.nome, exercicio.carga, exercicio.repeticoes, exercicio.series, exercicio.comentario)

    def run(self):
        self.root.mainloop()

fichas = []
view = view_criar_ficha(fichas)
view.run()

print(fichas[0].nome_ficha)