from tkinter import Tk, Label, Entry, Button, Frame, StringVar, ttk, Text, Scrollbar, Canvas
import tkinter as tk
from Ficha import Ficha 
# from view_criar_ficha import view_criar_ficha

class view_criar_treino:

    def __init__(self):
        self.root = Tk()
        self.criar_treinos_entries = []
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

        i=0
        Label(content_frame, text="Criar treino", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)
        i+=1

        Label(content_frame, text="Nome aluno:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        Label(content_frame, text="Nome do caboco", font=fonte, bg=cor_de_fundo).grid(row=i, column=1, pady=5)
        i+=1

        Label(frame, text="Data de início:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        self.criar_treinos_entries.append(Entry(frame, font=fonte))
        self.criar_treinos_entries[-1].bind("<KeyRelease>", self.formatar_como_data)
        self.criar_treinos_entries[-1].grid(row=i, column=1, pady=5)
        i+=1

        Label(frame, text="Data de finalização:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        self.criar_treinos_entries.append(Entry(frame, font=fonte))
        self.criar_treinos_entries[-1].bind("<KeyRelease>", self.formatar_como_data)
        self.criar_treinos_entries[-1].grid(row=i, column=1, pady=5)

        Label(content_frame, text="Quantidade de fichas:", font=fonte, bg=cor_de_fundo).grid(row=i, column=0, pady=5)
        opcoes_cbx = ["2", "3", "4"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(content_frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, state="readonly")
        cbx_combobox.grid(row=i, column=1, pady=5)
        self.login_entries.append(cbx_combobox)
        i+=1

        botao_quant = Button(content_frame, text="Criar treinos", command=criar_fichas_def(cbx_combobox, i+1), font=fonte, bg="#4CAF50", fg="white")
        botao_quant.grid(row=i, column=0, columnspan=2, pady=10)
        i+=1

        vet_fichas = []
        vet_buttons = []
        def criar_fichas_def(cbx_combobox, i):
            # vet_button = [Button(content_frame, text="Criar ficha "+str(quant+1), command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white") for quant in range(0, cbx_combobox)]
            for quant in range(0, cbx_combobox):
                # ficha = view_criar_ficha()
                # vet_fichas.append(ficha)
                print("ficha")

                # Button(content_frame, text="Criar ficha "+str(quant+1), command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white").grid(row=13, column=0, columnspan=2, pady=10)

            for quant in range(0, cbx_combobox):
                vet_buttons.append(Button(content_frame, text="Editar ficha "+str(quant+1), command=self.editar_ficha(vet_fichas, quant), font=fonte, bg="#4CAF50", fg="white"))
                vet_buttons[quant].grid(row=i, column=0, columnspan=2, pady=10)
                i+=1

        i+=cbx_combobox

        

        botao_salvar = Button(content_frame, text="Salvar treino", command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white")
        botao_salvar.grid(row=13, column=0, columnspan=2, pady=10)
        i+=1


        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))



    def editar_ficha(self, vet_fichas, quant):
        # vet_fichas[quant] = view_criar_ficha()
        pass

    def show_login_screen(self):
        # Mostra novamente a tela de login
        self.root.deiconify()

    def formatar_como_data(self, event):
        texto = self.cadastro_entries[3].get()

        # Adiciona barras automaticamente enquanto o usuário digita
        if len(texto) == 2 or len(texto) == 5:
            self.cadastro_entries[3].insert(tk.END, '/')

view_criar_treino()