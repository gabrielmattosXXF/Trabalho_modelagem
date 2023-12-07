import json
from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, messagebox
from cadastrar import Cadastro
from view_inicio_aluno import view_inicio_aluno
from view_inicio_personal import view_inicio_personal


class Login:
    def __init__(self):
        self.root = Tk()
        self.login_entries = []
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
        self.root.title("Tela de Login")

        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(pady=20)

        Label(frame, text="Tela de Login", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2,
                                                                                         pady=10)

        Label(frame, text="Email:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte))
        self.login_entries[0].grid(row=1, column=1, pady=5)

        Label(frame, text="Senha:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte, show="*"))
        self.login_entries[1].grid(row=2, column=1, pady=5)

        login_button = Button(frame, text="Login", command=self.login, bg="#4CAF50", fg="white", font=fonte)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        texto_cadastrar = Label(frame, text="Cadastrar", font=fonte, bg=cor_de_fundo, fg="blue", cursor="hand2")
        texto_cadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        texto_cadastrar.bind("<Button-1>", lambda event: self.show_registration_screen())

    def show_registration_screen(self):
        # Esconde a tela de login
        self.root.withdraw()

        # Cria uma nova janela para a tela de cadastro
        registration_window = Toplevel(self.root)
        Cadastro(registration_window, self.root)  # Passa o Toplevel como argumento

    def login(self):
        # Obtém os dados do formulário
        email = self.login_entries[0].get()
        senha = self.login_entries[1].get()

        # Verifica se o email e a senha foram fornecidos
        if not email or not senha:
            messagebox.showerror("Erro", "Por favor, insira o email e a senha.")
            return

        # Verifica se o usuário existe nos arquivos JSON correspondentes
        aluno_id = self.verificar_usuario("aluno.json", email, senha)
        personal_id = self.verificar_usuario("personal.json", email, senha)

        if aluno_id != 0:
            self.show_aluno_screen(aluno_id)
        elif personal_id != 0:
            self.show_personal_screen(personal_id)
        else:
            # Exibe uma mensagem de erro se o usuário não for encontrado
            messagebox.showerror("Erro", "Usuário não encontrado ou senha incorreta.")

    def verificar_usuario(self, nome_arquivo, email, senha):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            return False  # Retorna False se o arquivo não existir

        # Procura o usuário com o email e senha fornecidos
        for usuario in dados.get("usuarios", []):
            if usuario["email"] == email and usuario["senha"] == senha:
                return usuario["id"]  # Retorna True se o usuário for encontrado

        return 0  # Retorna False se o usuário não for encontrado

    def show_aluno_screen(self,aluno_id):
        # Esconde a tela de login
        self.root.withdraw()

        # Cria uma nova janela para a tela de cadastro
        aluno_window = Toplevel(self.root)
        view_inicio_aluno(aluno_window, self.root, aluno_id)  # Passa o Toplevel como argumento
    def show_personal_screen(self, personal_id):
        # Esconde a tela de login
        self.root.withdraw()

        # Cria uma nova janela para a tela de cadastro
        personal_window = Toplevel(self.root)
        view_inicio_personal(personal_window, self.root, personal_id)  # Passa o Toplevel como argumento

Login()
