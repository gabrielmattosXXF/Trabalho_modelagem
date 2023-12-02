import tkinter as tk
from tkinter import messagebox

def entrar():
    email = entry_email.get()
    senha = entry_senha.get()

    # Lógica de autenticação (substitua com sua própria lógica)
    if email == "usuario@example.com" and senha == "senha123":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Falha no login. Verifique seu email e senha.")

def abrir_janela_cadastro():
    # Fechar a janela de login
    janela.withdraw()

    # Criar uma nova janela para o cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro")

    # Configurações de Estilo
    cor_de_fundo = "#f0f0f0"
    fonte = ("Helvetica", 12)

    # Configurações de Tamanho e Posição
    largura_janela_cadastro = 400
    altura_janela_cadastro = 600

    largura_tela_cadastro = janela_cadastro.winfo_screenwidth()
    altura_tela_cadastro = janela_cadastro.winfo_screenheight()

    x_pos_cadastro = (largura_tela_cadastro - largura_janela_cadastro) // 2
    y_pos_cadastro = (altura_tela_cadastro - altura_janela_cadastro) // 2

    janela_cadastro.geometry(f"{largura_janela_cadastro}x{altura_janela_cadastro}+{x_pos_cadastro}+{y_pos_cadastro}")

    janela_cadastro.configure(bg=cor_de_fundo)

    # Adicionar botão para voltar à tela de login
    # botao_voltar = tk.Button(janela_cadastro, text="Já cadastrado? Entre aqui", command=voltar_login, font=fonte, bg="blue", fg="white", cursor="hand2")
    # botao_voltar.pack(pady=10)

    # Adicionar texto "Já é cadastrado? Entre aqui" que abre a janela de login
    texto_voltar = tk.Label(janela_cadastro, text="Já é cadastrado? Entre aqui", font=fonte, bg=cor_de_fundo, fg="blue", cursor="hand2")
    texto_voltar.pack(pady=10)
    texto_voltar.bind("<Button-1>", lambda event: voltar_login())

    # Adicionar componentes à janela de cadastro
    label_nome = tk.Label(janela_cadastro, text="Nome:", font=fonte, bg=cor_de_fundo)
    label_nome.pack(pady=5)

    entry_nome = tk.Entry(janela_cadastro, font=fonte)
    entry_nome.pack(pady=5)

    label_email = tk.Label(janela_cadastro, text="Email:", font=fonte, bg=cor_de_fundo)
    label_email.pack(pady=5)

    entry_email = tk.Entry(janela_cadastro, font=fonte)
    entry_email.pack(pady=5)

    label_senha = tk.Label(janela_cadastro, text="Senha:", font=fonte, bg=cor_de_fundo)
    label_senha.pack(pady=5)

    entry_senha = tk.Entry(janela_cadastro, show="*", font=fonte)
    entry_senha.pack(pady=5)

    label_data_nascimento = tk.Label(janela_cadastro, text="Data de Nascimento:", font=fonte, bg=cor_de_fundo)
    label_data_nascimento.pack(pady=5)

    entry_data_nascimento = tk.Entry(janela_cadastro, font=fonte)
    entry_data_nascimento.pack(pady=5)

    label_tipo_usuario = tk.Label(janela_cadastro, text="Tipo de Usuário:", font=fonte, bg=cor_de_fundo)
    label_tipo_usuario.pack(pady=5)

    # Opções para o combobox (tipo de usuário)
    opcoes_tipo_usuario = ["Aluno", "Personal Trainer"]
    var_tipo_usuario = tk.StringVar(janela_cadastro)
    var_tipo_usuario.set(opcoes_tipo_usuario[0])  # Define o valor padrão

    combo_tipo_usuario = tk.OptionMenu(janela_cadastro, var_tipo_usuario, *opcoes_tipo_usuario)
    combo_tipo_usuario.pack(pady=10)

    botao_cadastrar = tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar, font=fonte, bg="#4CAF50", fg="white")
    botao_cadastrar.pack(pady=10)

    # Função para cadastrar
    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        data_nascimento = entry_data_nascimento.get()
        tipo_usuario = var_tipo_usuario.get()

        # Lógica de cadastro (substitua com sua própria lógica)
        messagebox.showinfo("Cadastro", f"Cadastro bem-sucedido!\nNome: {nome}\nEmail: {email}\nTipo de Usuário: {tipo_usuario}")

    # Função para voltar à tela de login
    def voltar_login():

        # Tornar visível a janela de login
        janela.deiconify()

        # Destruir a janela de cadastro
        janela_cadastro.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# Configurações de Estilo
cor_de_fundo = "#f0f0f0"
cor_botoes = "#4CAF50"
fonte = ("Helvetica", 12)

# Configurações de Tamanho e Posição
largura_janela = 400
altura_janela = 300

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

janela.configure(bg=cor_de_fundo)

# Adicionar componentes à janela
label_email = tk.Label(janela, text="Email:", font=fonte, bg=cor_de_fundo)
label_email.pack(pady=5)

entry_email = tk.Entry(janela, font=fonte)
entry_email.pack(pady=5)

label_senha = tk.Label(janela, text="Senha:", font=fonte, bg=cor_de_fundo)
label_senha.pack(pady=5)

entry_senha = tk.Entry(janela, show="*", font=fonte)
entry_senha.pack(pady=5)

botao_entrar = tk.Button(janela, text="Entrar", command=entrar, font=fonte, bg=cor_botoes, fg="white")
botao_entrar.pack(pady=10)

# Adicionar texto "Cadastrar" que abre a janela de cadastro
texto_cadastrar = tk.Label(janela, text="Cadastrar", font=fonte, bg=cor_de_fundo, fg="blue", cursor="hand2")
texto_cadastrar.pack(pady=10)
texto_cadastrar.bind("<Button-1>", lambda event: abrir_janela_cadastro())

# Iniciar o loop principal
janela.mainloop()