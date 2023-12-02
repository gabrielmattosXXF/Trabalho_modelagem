from tkinter import Tk, Label, Entry, Button, Frame, Toplevel

class TelaInicialAluno:
    def __init__(self,aluno):
        self.root = Tk()
        self.aluno = aluno
        self.screen()
        self.create_widgets()
        self.root.mainloop()

    def screen(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        # Configurações de Tamanho e Posição
        largura_janela = 400
        altura_janela = 300

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Tela de Início de " + self.aluno.nome)

        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(pady=20)

        Label(frame, text="Tela de Início de " + self.aluno.nome, font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)

        Label(frame, text="Email:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte))
        self.login_entries[0].grid(row=1, column=1, pady=5)

        Label(frame, text="Senha:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte, show="*"))
        self.login_entries[1].grid(row=2, column=1, pady=5)

        Treino_button = Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=fonte)
        Treino_button.grid(row=3, column=0, columnspan=2, pady=10)

        VerPerfil_button = Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=fonte)
        VerPerfil_button.grid(row=3, column=0, columnspan=2, pady=10)

        VerPersonal_button = Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=fonte)
        VerPersonal_button.grid(row=3, column=0, columnspan=2, pady=10)

        VerFichaMedica_button = Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=fonte)
        VerFichaMedica_button.grid(row=3, column=0, columnspan=2, pady=10)

        texto_cadastrar = Label(frame, text="Cadastrar", font=fonte, bg=cor_de_fundo, fg="blue", cursor="hand2")
        texto_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        texto_cadastrar.bind("<Button-1>", lambda event: self.show_registration_screen())

    def login(self):
        # Adicione a lógica de login aqui
        print("Login Button Clicked")

    def show_registration_screen(self):
        # Esconde a tela de login
        self.root.withdraw()

        # Cria uma nova janela para a tela de cadastro
        registration_window = Toplevel(self.root)
        Cadastro(registration_window, self.root)  # Passa o Toplevel como argumento


Login()
