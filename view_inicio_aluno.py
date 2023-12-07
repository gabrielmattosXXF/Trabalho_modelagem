from datetime import datetime
from tkinter import Label, Entry, Button, Frame, StringVar, ttk, messagebox
import tkinter as tk
import json
from Usuario import Usuario
from Aluno import Aluno

class view_inicio_aluno:
    def __init__(self, parent, root_pai, user_id):
        self.root = parent
        self.root_pai = root_pai
        self.aluno = self.buscar_usuarios_por_id("aluno", user_id)
        self.user_id = user_id
        self.create_widgets()
        self.screen()

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
        self.root.title("Aluno")

        self.root.configure(bg=cor_de_fundo)

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        # Cabeçalho com o nome do aluno e botão para deslogar
        frame_cabecalho = Frame(self.root, bg=cor_de_fundo)
        frame_cabecalho.grid(row=0, column=0, sticky="ew", pady=10)

        # Label(frame_cabecalho, text=f"Bem-vindo, {self.aluno.get_nome()}!", font=("Helvetica", 16), bg=cor_de_fundo).grid(
        #     row=0, column=0, padx=20, sticky="w")
        Label(frame_cabecalho, text=f"Bem-vindo, Juanita!", font=("Helvetica", 16), bg=cor_de_fundo).grid(
            row=0, column=0, padx=20, sticky="w")

        # Empty label to push the "Deslogar" button to the right
        Label(frame_cabecalho, text="", bg=cor_de_fundo, width=27).grid(row=0, column=1, sticky="ew")

        # Botão para deslogar
        deslogar_button = Button(frame_cabecalho, text="Deslogar", command=self.deslogar, bg="#e74c3c", fg="white",
                                 font=fonte)
        deslogar_button.grid(row=0, column=2, padx=10, sticky="e")

        # Parte principal da tela com 6 botões de funções
        frame_principal = Frame(self.root, bg=cor_de_fundo)
        frame_principal.grid(row=1, column=0, pady=20)

        # Botão 1 - Exemplo (substitua com suas próprias funções)
        botao1 = Button(frame_principal, text="Visualizar treino atual", command=self.funcao1, bg="#3498db", fg="white", font=fonte, width=25)
        botao1.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Botão 2 - Exemplo
        botao2 = Button(frame_principal, text="Vizualizar treinos anteriores", command=self.funcao2, bg="#3498db", fg="white", font=fonte, width=25)
        botao2.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        # Botão 3 - Exemplo
        botao3 = Button(frame_principal, text="Visualizar personal", command=self.funcao3, bg="#3498db", fg="white", font=fonte, width=25)
        botao3.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        # Botão 4 - Exemplo
        botao4 = Button(frame_principal, text="Solicitar atendimento", command=self.funcao4, bg="#3498db", fg="white", font=fonte, width=25)
        botao4.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

        # Botão 5 - Exemplo
        botao5 = Button(frame_principal, text="Visualizar agenda", command=self.funcao5, bg="#3498db", fg="white", font=fonte, width=25)
        botao5.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

        # Botão 6 - Exemplo
        botao6 = Button(frame_principal, text="Adicionar ficha médica", command=self.funcao6, bg="#3498db", fg="white", font=fonte, width=25)
        botao6.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")

        # Configurar as proporções de coluna e linha para que os elementos centrais se expandam
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        frame_principal.grid_columnconfigure((0, 1), weight=1)

    def deslogar(self):
        # Fecha a tela de cadastro e mostra novamente a tela de login
        self.root.destroy()
        self.root_pai.deiconify()

    def funcao1(self):
        print("func1")
    def funcao2(self):
        print("func2")
    def funcao3(self):
        print("func3")
    def funcao4(self):
        print("func4")
    def funcao5(self):
        print("func5")

    def funcao6(self):
        print("func6")
    def buscar_usuarios_por_id(self, tipo_alvo, id_alvo):
            
        from main import vet_usuarios
        for user in vet_usuarios:
            if getattr(user, "id") == id_alvo and getattr(user, "tipo_usuario") == tipo_alvo:
                data_nasc_obj = datetime.strptime(getattr(user, "idade"), "%d/%m/%Y")

                # Obtém a data atual
                data_atual = datetime.now()

                # Calcula a diferença em anos
                idade = data_atual.year - data_nasc_obj.year - (
                            (data_atual.month, data_atual.day) < (data_nasc_obj.month, data_nasc_obj.day))
                user.idade = idade
                return Aluno(user, None, None)
            else:
                print(f"Usuário com ID {id_alvo} não encontrado.")
                return None

# view_inicio_aluno(tk.Tk(), None, 1)