from tkinter import Label, Entry, Button, Frame, StringVar, ttk, messagebox
import tkinter as tk
import json


class Cadastro:
    def __init__(self, parent, root_pai):
        self.root = parent
        self.root_pai = root_pai
        self.cbx_var = None
        self.contador_id = 0
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

        Label(frame, text="Tela de Cadastro", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0,
                                                                                            columnspan=2, pady=10)

        Label(frame, text="Nome:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte))
        self.cadastro_entries[0].grid(row=1, column=1, pady=5)

        Label(frame, text="Email:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte))
        self.cadastro_entries[1].grid(row=2, column=1, pady=5)

        Label(frame, text="Senha:", font=fonte, bg=cor_de_fundo).grid(row=3, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte, show="*"))
        self.cadastro_entries[2].grid(row=3, column=1, pady=5)

        Label(frame, text="Data de Nascimento:", font=fonte, bg=cor_de_fundo).grid(row=4, column=0, pady=5)
        self.cadastro_entries.append(Entry(frame, font=fonte))
        self.cadastro_entries[3].bind("<KeyRelease>", self.formatar_como_data)
        self.cadastro_entries[3].grid(row=4, column=1, pady=5)

        # Nova combobox chamada "cbx"
        Label(frame, text="Tipo de Usuário:", font=fonte, bg=cor_de_fundo).grid(row=5, column=0, pady=5)
        opcoes_cbx = ["Aluno", "Personal trainer"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, width=15,
                                    state="readonly")
        cbx_combobox.grid(row=5, column=1, pady=5)

        cadastrar_button = Button(frame, text="Cadastrar", command=self.cadastrar, bg="#3498db", fg="white", font=fonte)
        cadastrar_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Texto clicável para retornar à tela de login
        texto_login = Label(frame, text="Já possui um cadastro? Faça login", font=fonte, bg=cor_de_fundo, fg="blue",
                            cursor="hand2")
        texto_login.grid(row=7, column=0, columnspan=2, pady=10)
        texto_login.bind("<Button-1>", lambda event: self.desistir())

    def cadastrar(self):
        # Aqui você pode adicionar a lógica para processar os dados do cadastro
        # Neste exemplo, exibimos uma mensagem com os dados inseridos
        self.handle_cadastrar()

    def desistir(self):
        # Fecha a tela de cadastro e mostra novamente a tela de login
        self.root.destroy()
        self.root_pai.deiconify()

    def handle_cadastrar(self):
        # Obtém os dados do formulário
        nome = self.cadastro_entries[0].get()
        email = self.cadastro_entries[1].get()
        senha = self.cadastro_entries[2].get()
        data_nascimento = self.cadastro_entries[3].get()
        tipo_usuario = self.cbx_var.get()

        # Verifica se todos os campos foram preenchidos
        if not email or not senha or not data_nascimento:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        # Obtém o último ID salvo no arquivo JSON correspondente
        if tipo_usuario == "Aluno":
            ultimo_id = self.obter_ultimo_id("aluno")
        else:
            ultimo_id = self.obter_ultimo_id("personal")

        # Incrementa o contador de ID
        id_usuario = ultimo_id + 1

        # Cria um dicionário com os dados do usuário
        novo_usuario = {
            "id": id_usuario,
            "nome": nome,
            "email": email,
            "senha": senha,
            "data_nascimento": data_nascimento,
            "tipo_usuario": tipo_usuario
        }

        # Adiciona o usuário ao arquivo JSON correspondente
        if tipo_usuario == "Aluno":
            self.adicionar_usuario("aluno.json", novo_usuario)
        elif tipo_usuario == "Personal trainer":
            self.adicionar_usuario("personal.json", novo_usuario)

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Cadastro Realizado", "Cadastro realizado com sucesso!")

    def obter_ultimo_id(self, tipo_usuario):
        # Tenta carregar os dados do arquivo JSON correspondente
        try:
            with open(f"{tipo_usuario.lower()}.json", 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            return 0  # Retorna 0 se o arquivo não existir

        # Verifica se há usuários no arquivo
        if "usuarios" in dados and dados["usuarios"]:
            # Ordena os usuários pelo ID em ordem decrescente e retorna o ID do primeiro usuário
            usuarios_ordenados = sorted(dados["usuarios"], key=lambda x: x["id"], reverse=True)
            return usuarios_ordenados[0]["id"]
        else:
            return 0  # Retorna 0 se não houver usuários no arquivo

    def adicionar_usuario(self, nome_arquivo, usuario):
        # Carrega os dados existentes do arquivo JSON
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = {"usuarios": []}

        # Adiciona o novo usuário aos dados existentes
        dados["usuarios"].append(usuario)

        # Salva os dados atualizados no arquivo JSON
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)

    def formatar_como_data(self, event):
        texto = self.cadastro_entries[3].get()

        # Adiciona barras automaticamente enquanto o usuário digita
        if len(texto) == 2 or len(texto) == 5:
            self.cadastro_entries[3].insert(tk.END, '/')
