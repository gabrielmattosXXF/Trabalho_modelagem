from tkinter import Tk, Label, Entry, Button, Frame, StringVar, ttk, Canvas
import tkinter as tk
from view_criar_ficha import view_criar_ficha
from view_editar_ficha import view_editar_ficha

class view_criar_ficha:

    def __init__(self):
        self.root = Tk()
        self.criar_treinos_entries = []
        self.vet_fichas = []  # Lista para armazenar as instâncias de view_criar_ficha
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

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

        i = 0
        Label(content_frame, text="Criar treino", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=i, column=0, columnspan=2, pady=10)
        i += 1

        Label(content_frame, text="Nome aluno:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        Label(content_frame, text="Nome do caboco", font=fonte, bg=cor_de_fundo).grid(row=i, column=1, pady=5)
        i += 1

        Label(content_frame, text="Data de início:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        entry_inicio = Entry(content_frame, font=fonte)
        entry_inicio.bind("<KeyRelease>", self.formatar_como_data)
        entry_inicio.grid(row=i, column=1, pady=5)
        self.criar_treinos_entries.append(entry_inicio)
        i += 1

        Label(content_frame, text="Data de finalização:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        entry_final = Entry(content_frame, font=fonte)
        entry_final.bind("<KeyRelease>", self.formatar_como_data)
        entry_final.grid(row=i, column=1, pady=5)
        self.criar_treinos_entries.append(entry_final)
        i+=1

        Label(content_frame, text="Quantidade de fichas:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        opcoes_cbx = ["2", "3", "4"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(content_frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, state="readonly")
        cbx_combobox.grid(row=i, column=1, pady=5)
        i += 1

        verif = [0]
        botao_quant = Button(content_frame, text="Criar treinos", command=lambda: self.criar_fichas_def(cbx_combobox, verif), font=fonte, bg="#4CAF50", fg="white")
        botao_quant.grid(row=i, column=0, columnspan=2, pady=10)
        i += 1

        self.vet_fichas = []

        if verif[0] == 1:

            for quant in range(0, int(cbx_combobox.get())):
                self.vet_fichas.append(None)

            for quant in range(0, int(cbx_combobox.get())):
                botao_editar = Button(content_frame, text=f"Editar ficha {quant + 1}", command=lambda q=quant: self.editar_ficha(q), font=fonte, bg="#4CAF50", fg="white")
                botao_editar.grid(row=i, column=0, columnspan=2, pady=10)
                i += 1

            self.root.update_idletasks()

            botao_salvar = Button(content_frame, text="Salvar treino", command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white")
            botao_salvar.grid(row=i, column=0, columnspan=2, pady=10)
            i += 1

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def criar_fichas_def(self, cbx_combobox, verif):
        for quant in range(0, int(cbx_combobox.get())):
            ficha = view_criar_ficha()  # Substitua view_criar_ficha() pela classe correta ou função de criação
            self.vet_fichas.append(ficha)
        
        verif[-1] = 1

    def editar_ficha(self, quant):
        ficha = view_editar_ficha(ficha)  # Substitua view_criar_ficha() pela classe correta ou função de criação
        self.vet_fichas[quant] = ficha

    def salvar_ficha(self):
        # Adicione sua lógica para salvar as informações do treino e das fichas
        pass

    def formatar_como_data(self, event):
        texto = self.criar_treinos_entries[-1].get()

        # Adiciona barras automaticamente enquanto o usuário digita
        if len(texto) == 2 or len(texto) == 5:
            self.criar_treinos_entries[-1].insert(tk.END, '/')

        texto2 = self.criar_treinos_entries[-2].get()

        # Adiciona barras automaticamente enquanto o usuário digita
        if len(texto2) == 2 or len(texto2) == 5:
            self.criar_treinos_entries[-2].insert(tk.END, '/')

# Inicialização da aplicação
view_criar_ficha()