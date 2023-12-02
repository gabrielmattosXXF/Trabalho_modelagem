from tkinter import Label, Entry, Button, Frame, StringVar, ttk, messagebox

class Cadastro:
    def __init__(self, parent, root_pai):
        self.root = parent
        self.root_pai = root_pai
        self.cbx_var = None
        self.cadastro_entries = []
        self.screen()
        self.create_widgets()

    def screen(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        # Configurações de Tamanho e Posição
        largura_janela = 400
        altura_janela = 350

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Tela de Cadastro")

        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(pady=20)

        Label(frame, text="Tela de Cadastro", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)

        Label(frame, text="Email:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte))
        self.cadastro_entries[0].grid(row=1, column=1, pady=5)

        Label(frame, text="Senha:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte, show="*"))
        self.cadastro_entries[1].grid(row=2, column=1, pady=5)

        Label(frame, text="Data de Nascimento:", font=fonte, bg=cor_de_fundo).grid(row=3, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte))
        self.cadastro_entries[2].grid(row=3, column=1, pady=5)

        # Nova combobox chamada "cbx"
        Label(frame, text="Tipo de Usuário:", font=fonte, bg=cor_de_fundo).grid(row=5, column=0, pady=5)
        opcoes_cbx = ["Aluno", "Personal trainer"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, width= 15, state="readonly")
        cbx_combobox.grid(row=5, column=1, pady=5)

        cadastrar_button = Button(frame, text="Cadastrar", command=self.cadastrar, bg="#3498db", fg="white", font=fonte)
        cadastrar_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Texto clicável para retornar à tela de login
        texto_login = Label(frame, text="Já possui um cadastro? Faça login", font=fonte, bg=cor_de_fundo, fg="blue", cursor="hand2")
        texto_login.grid(row=7, column=0, columnspan=2, pady=10)
        texto_login.bind("<Button-1>", lambda event: self.desistir())

    def cadastrar(self):
        # Aqui você pode adicionar a lógica para processar os dados do cadastro
        # Neste exemplo, exibimos uma mensagem com os dados inseridos
        mensagem = f"Email: {self.cadastro_entries[0].get()}\nSenha: {self.cadastro_entries[1].get()}\nData de Nascimento: {self.cadastro_entries[2].get()}\nTipo: {self.cbx_var.get()}"
        messagebox.showinfo("Cadastro Realizado", mensagem)

    def desistir(self):
        # Fecha a tela de cadastro e mostra novamente a tela de login
        self.root.destroy()
        self.root_pai.deiconify()