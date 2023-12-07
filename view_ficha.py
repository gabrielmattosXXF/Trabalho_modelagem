from tkinter import Tk, Label, Button, Frame, StringVar, ttk, Text, Scrollbar, Canvas
import tkinter as tk
from Ficha import Ficha

class view_ficha:

    def __init__(self, ficha):
        self.ficha_treino = ficha
        self.root = Tk()
        self.login_entries = []
        self.screen()
        self.create_widgets()
        self.root.mainloop()

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
        self.root.title("Ficha")
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

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

        i = 0
        Label(content_frame, text=self.ficha_treino.nome_ficha, font=("Helvetica", 16), bg=cor_de_fundo).grid(row=i, column=0, columnspan=2, pady=10)
        i += 1

        for exerc in self.ficha_treino.exercicios.values():
            Label(content_frame, text=exerc.nome, font=("Helvetica", 16), bg=cor_de_fundo).grid(row=i, column=0, columnspan=2, pady=10)
            i += 1

            labels_info = {"Carga:":"carga", "Repetições:":"repeticoes", "Séries:":"series"}
            for label_info, value in labels_info.items():
                Label(content_frame, text=label_info, font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
                Label(content_frame, text=getattr(exerc, value), font=fonte, bg=cor_de_fundo).grid(row=i, column=1, pady=5)
                i += 1

            Label(content_frame, text="Comentário:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
            text_comentario = Text(content_frame, height=4, width=30, font=fonte)
            text_comentario.grid(row=i, column=1, pady=5)
            text_comentario.insert("1.0", exerc.comentario)
            text_comentario.config(state="disabled")
            scrollbar_problemas = Scrollbar(content_frame, command=text_comentario.yview)
            scrollbar_problemas.grid(row=i, column=2, sticky="nsew")
            text_comentario.config(yscrollcommand=scrollbar_problemas.set)
            i += 1

        botao_retornar = Button(content_frame, text="Retornar para Treino", command=self.retornar_para_treino, font=fonte, bg="#3498db", fg="white")
        botao_retornar.grid(row=i, column=0, columnspan=2, pady=10)

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def atualizar_exercicios(self):
        # Limpar a tela antes de atualizar
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        i = 0
        Label(self.content_frame, text=self.ficha_treino.nome_ficha, font=("Helvetica", 16), bg="#f0f0f0").grid(row=i, column=0, columnspan=2, pady=10)
        i += 1

        for exerc in self.ficha_treino.exercicios.values():
            Label(self.content_frame, text=exerc.nome, font=("Helvetica", 16), bg="#f0f0f0").grid(row=i, column=0, columnspan=2, pady=10)
            i += 1

            labels_info = {"Carga:":"carga", "Repetições:":"repeticoes", "Séries:":"series"}
            for label_info, value in labels_info.items():
                Label(self.content_frame, text=label_info, font=("Helvetica", 12), bg="#f0f0f0").grid(row=i, column=0, pady=5)
                Label(self.content_frame, text=getattr(exerc, value), font=("Helvetica", 12), bg="#f0f0f0").grid(row=i, column=1, pady=5)
                i += 1

            Label(self.content_frame, text="Comentário:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=i, column=0, pady=5)
            text_comentario = Text(self.content_frame, height=4, width=30, font=("Helvetica", 12), state="disabled")
            text_comentario.grid(row=i, column=1, pady=5)
            text_comentario.insert("1.0", exerc.comentario)
            text_comentario.config(state="disabled")
            scrollbar_problemas = Scrollbar(self.content_frame, command=text_comentario.yview)
            scrollbar_problemas.grid(row=i, column=2, sticky="nsew")
            text_comentario.config(yscrollcommand=scrollbar_problemas.set)
            i += 1

        botao_retornar = Button(self.content_frame, text="Retornar para Treino", command=self.retornar_para_treino, font=("Helvetica", 12), bg="#3498db", fg="white")
        botao_retornar.grid(row=i, column=0, columnspan=2, pady=10)

        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def salvar_ficha(self):
        print("Informações salvas!")

    def retornar_para_treino(self):
        self.root.destroy()  # Destruir a janela atual
        import view_treino  # Importar aqui para evitar a circularidade
        view_treino.view_treino()  # Chamar a classe view_treino novamente

    def show_login_screen(self):
        # Mostra novamente a tela de login
        self.root.deiconify()

if __name__ == "__main__":
    ficha = Ficha("Ficha 1")
    ficha.adicionar_exercicio("Supino", 50, 10, 3, "Comentário 1")
    ficha.adicionar_exercicio("Rosca direta", 10, 10, 3, "Comentário 2")
    ficha.adicionar_exercicio("Tríceps", 10, 10, 3, "Comentário 3")
    ficha.adicionar_exercicio("Supina", 50, 10, 3, "Comentário 1")
    ficha.adicionar_exercicio("Rosca adentro", 10, 10, 3, "Comentário 2")
    ficha.adicionar_exercicio("Tripas", 10, 10, 3, "Comentário 3")

    view_ficha(ficha)