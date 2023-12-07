from tkinter import Tk, Label, Entry, Button, Frame, StringVar, OptionMenu, Text, Scrollbar, ttk
from Ficha import Ficha

class view_exercicio:
    def __init__(self):
        self.root = Tk()
        self.exercicio_entries = []
        self.ficha = Ficha("Minha ficha")
        self.screen()
        self.create_widgets()
        self.root.mainloop()

    def screen(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        # Configurações de Tamanho e Posição
        largura_janela = 600
        altura_janela = 600

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Exercicio")
        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(pady=20)

        Label(frame, text="Adicionar Exercício", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)

        Label(frame, text="Nome:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.exercicio_entries.append(Entry(frame, font=fonte))
        self.exercicio_entries[0].grid(row=1, column=1, pady=5)

        Label(frame, text="Carga:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.exercicio_entries.append(Entry(frame, font=fonte))
        self.exercicio_entries[1].grid(row=2, column=1, pady=5)

        Label(frame, text="Repetições:", font=fonte, bg=cor_de_fundo).grid(row=3, column=0, pady=5)
        self.exercicio_entries.append(Entry(frame, font=fonte))
        self.exercicio_entries[2].grid(row=3, column=1, pady=5)

        Label(frame, text="Serie:", font=fonte, bg=cor_de_fundo).grid(row=4, column=0, pady=5)
        opcoes_cbx = ["1", "2", "3", "4"]
        cbx_var = StringVar()
        cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(frame, textvariable=cbx_var, values=opcoes_cbx, font=fonte, state="readonly")
        cbx_combobox.grid(row=4, column=1, pady=5)
        self.exercicio_entries.append(cbx_combobox)

        Label(frame, text="Comentário:", font=fonte, bg=cor_de_fundo).grid(row=5, column=0, pady=5)
        text_comentario = Text(frame, height=4, width=30, font=fonte)
        text_comentario.grid(row=5, column=1, pady=5)
        scrollbar_comentario = Scrollbar(frame, command=text_comentario.yview)
        scrollbar_comentario.grid(row=5, column=2, sticky="nsew")
        text_comentario.config(yscrollcommand=scrollbar_comentario.set)
        self.exercicio_entries.append(text_comentario)

        botao_salvar = Button(frame, text="Adicionar", command=self.salvar_exercicio, font=fonte, bg="#4CAF50", fg="white")
        botao_salvar.grid(row=6, column=0, columnspan=2, pady=10)

    # def salvar_exercicio(self):
    #     print("Informações salvas:")
    #     print("Nome:", self.exercicio_entries[0].get())
    #     print("Carga:", self.exercicio_entries[1].get())
    #     print("Repetições:", self.exercicio_entries[2].get())
    #     print("Série:", self.exercicio_entries[3].get())
    #     print("Comentário:", self.exercicio_entries[4].get("1.0", "end-1c"))

    def salvar_exercicio(self):
        nome = self.exercicio_entries[0].get()
        carga = self.exercicio_entries[1].get()
        repeticoes = self.exercicio_entries[2].get()
        serie = self.exercicio_entries[3].get()
        comentario = self.exercicio_entries[4].get("1.0", "end-1c")

        # Use the Ficha class to add the exercise
        self.ficha.adicionar_exercicio(nome, carga, repeticoes, serie, comentario)

        print("Informações salvas:")
        print("Nome:", nome)
        print("Carga:", carga)
        print("Repetições:", repeticoes)
        print("Série:", serie)
        print("Comentário:", comentario)
        print("Ficha JSON:")
    
        print(self.ficha.to_json())
    
    #ficha = Ficha("Minha Ficha")


view_exercicio()