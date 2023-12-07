from tkinter import Tk, Label, Entry, Button, Frame, StringVar, ttk, Text, Scrollbar, Canvas
import tkinter as tk

class view_ficha_medica:

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
        largura_janela = 500
        altura_janela = 600

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Ficha médica")
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


        Label(content_frame, text="Ficha médica", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)

        Label(content_frame, text="Nome:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        Label(content_frame, text="Nome do caboco", font=fonte, bg=cor_de_fundo).grid(row=1, column=1, pady=5)

        Label(content_frame, text="Sexo:", font=fonte, bg=cor_de_fundo).grid(row=3, column=0, pady=5)
        opcoes_cbx = ["Masculino", "Feminino", "Outro"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(content_frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, state="readonly")
        cbx_combobox.grid(row=3, column=1, pady=5)
        self.login_entries.append(cbx_combobox)

        Label(content_frame, text="Altura:", font=fonte, bg=cor_de_fundo).grid(row=4, column=0, pady=5)
        self.login_entries.append(Entry(content_frame, font=fonte))
        self.login_entries[1].grid(row=4, column=1, pady=5)

        Label(content_frame, text="Massa Branca:", font=fonte, bg=cor_de_fundo).grid(row=5, column=0, pady=5)
        self.login_entries.append(Entry(content_frame, font=fonte))
        self.login_entries[2].grid(row=5, column=1, pady=5)

        Label(content_frame, text="Percentual de Gordura:", font=fonte, bg=cor_de_fundo).grid(row=6, column=0, pady=5)
        self.login_entries.append(Entry(content_frame, font=fonte))
        self.login_entries[3].grid(row=6, column=1, pady=5)

        Label(content_frame, text="Problemas de Saúde:", font=fonte, bg=cor_de_fundo).grid(row=7, column=0, pady=5)
        text_problemas_saude = Text(content_frame, height=4, width=30, font=fonte)
        text_problemas_saude.grid(row=7, column=1, pady=5)
        scrollbar_problemas = Scrollbar(content_frame, command=text_problemas_saude.yview)
        scrollbar_problemas.grid(row=7, column=2, sticky="nsew")
        text_problemas_saude.config(yscrollcommand=scrollbar_problemas.set)
        self.login_entries.append(text_problemas_saude)

        Label(content_frame, text="Medicamentos em Uso:", font=fonte, bg=cor_de_fundo).grid(row=8, column=0, pady=5)
        text_medicamentos = Text(content_frame, height=4, width=30, font=fonte)
        text_medicamentos.grid(row=8, column=1, pady=5)
        scrollbar_medicamentos = Scrollbar(content_frame, command=text_medicamentos.yview)
        scrollbar_medicamentos.grid(row=8, column=2, sticky="nsew")
        text_medicamentos.config(yscrollcommand=scrollbar_medicamentos.set)
        self.login_entries.append(text_medicamentos)

        Label(content_frame, text="Histórico de lesões:", font=fonte, bg=cor_de_fundo).grid(row=9, column=0, pady=5)
        text_medicamentos = Text(content_frame, height=4, width=30, font=fonte)
        text_medicamentos.grid(row=9, column=1, pady=5)
        scrollbar_medicamentos = Scrollbar(content_frame, command=text_medicamentos.yview)
        scrollbar_medicamentos.grid(row=9, column=2, sticky="nsew")
        text_medicamentos.config(yscrollcommand=scrollbar_medicamentos.set)
        self.login_entries.append(text_medicamentos)

        Label(content_frame, text="Cirurgias:", font=fonte, bg=cor_de_fundo).grid(row=10, column=0, pady=5)
        text_medicamentos = Text(content_frame, height=4, width=30, font=fonte)
        text_medicamentos.grid(row=10, column=1, pady=5)
        scrollbar_medicamentos = Scrollbar(content_frame, command=text_medicamentos.yview)
        scrollbar_medicamentos.grid(row=10, column=2, sticky="nsew")
        text_medicamentos.config(yscrollcommand=scrollbar_medicamentos.set)
        self.login_entries.append(text_medicamentos)

        Label(content_frame, text="Contato de emergência:", font=fonte, bg=cor_de_fundo).grid(row=11, column=0, pady=5)
        self.login_entries.append(Entry(content_frame, font=fonte))
        self.login_entries[8].grid(row=11, column=1, pady=5)

        Label(content_frame, text="Telefone de emergência:", font=fonte, bg=cor_de_fundo).grid(row=12, column=0, pady=5)
        self.login_entries.append(Entry(content_frame, font=fonte))
        self.login_entries[9].grid(row=12, column=1, pady=5)

        botao_salvar = Button(content_frame, text="Salvar", command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white")
        botao_salvar.grid(row=13, column=0, columnspan=2, pady=10)


        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", on_configure)

        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))



    def salvar_ficha(self):
        # Aqui você pode adicionar a lógica para salvar ou processar as informações da ficha médica
        # Por exemplo, você pode exibir as informações em um messagebox para este exemplo
        print("Informações salvas:")
        print("Sexo:", self.login_entries[0].get())
        print("Altura:", self.login_entries[1].get())
        print("Massa Branca:", self.login_entries[2].get())
        print("Percentual de Gordura:", self.login_entries[3].get())
        print("Problemas de Saúde:", self.login_entries[4].get("1.0", "end-1c"))
        print("Medicamentos em Uso:", self.login_entries[5].get("1.0", "end-1c"))
        print("Histórico de lesões:", self.login_entries[6].get("1.0", "end-1c"))
        print("Cirurgias:", self.login_entries[7].get("1.0", "end-1c"))
        print("Contato de emergência:", self.login_entries[8].get())
        print("Telefone de emergência:", self.login_entries[9].get())

    def show_login_screen(self):
        # Mostra novamente a tela de login
        self.root.deiconify()

view_ficha_medica()
