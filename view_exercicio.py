from tkinter import Tk, Label, Entry, Button, Frame, Toplevel, StringVar, OptionMenu, Text, Scrollbar, ttk

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

        Label(frame, text="Exercício", font=("Helvetica", 16), bg=cor_de_fundo).grid(row=0, column=0, columnspan=2, pady=10)

        Label(frame, text="Nome:", font=fonte, bg=cor_de_fundo).grid(row=1, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte))
        self.login_entries[1].grid(row=1, column=1, pady=5)

        Label(frame, text="Carga:", font=fonte, bg=cor_de_fundo).grid(row=2, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte))
        self.login_entries[2].grid(row=2, column=1, pady=5)

        Label(frame, text="Repetições:", font=fonte, bg=cor_de_fundo).grid(row=3, column=0, pady=5)
        self.login_entries.append(Entry(frame, font=fonte))
        self.login_entries[3].grid(row=3, column=1, pady=5)

        label_serie = Label(frame, text="Serie:", font=fonte, bg=cor_de_fundo)
        label_serie.grid(row=4, column=0, pady=5)
        opcoes_cbx = ["1", "2", "3","4"]
        self.cbx_var = StringVar()
        self.cbx_var.set(opcoes_cbx[0])
        cbx_combobox = ttk.Combobox(frame, textvariable=self.cbx_var, values=opcoes_cbx, font=fonte, state="readonly")
        cbx_combobox.grid(row=4, column=1, pady=5)
        self.login_entries.append(cbx_combobox)
        self.login_entries[0].grid(row=4, column=1, pady=5)

        Label(frame, text="Comentário:", font=fonte, bg=cor_de_fundo).grid(row=5, column=0, pady=5)
        text_problemas_saude = Text(frame, height=4, width=30, font=fonte)
        text_problemas_saude.grid(row=5, column=1, pady=5)
        scrollbar_problemas = Scrollbar(frame, command=text_problemas_saude.yview)
        scrollbar_problemas.grid(row=5, column=2, sticky="nsew")
        text_problemas_saude.config(yscrollcommand=scrollbar_problemas.set)
        self.login_entries.append(text_problemas_saude)

        botao_salvar = Button(frame, text="Registrar", command=self.salvar_ficha, font=fonte, bg="#4CAF50", fg="white")
        botao_salvar.grid(row=7, column=0, columnspan=2, pady=10)

    def salvar_exercicio(self):
        # Aqui você pode adicionar a lógica para salvar ou processar as informações da ficha médica
        # Por exemplo, você pode exibir as informações em um messagebox para este exemplo
        print("Informações salvas:")
        print("Nome:", self.login_entries[0].get())
        print("Carga:", self.login_entries[1].get())
        print("Repetições:", self.login_entries[2].get())
        print("Percentual de Gordura:", self.login_entries[3].get())
        print("Problemas de Saúde:", self.login_entries[4].get("1.0", "end-1c"))
        print("Medicamentos em Uso:", self.login_entries[5].get("1.0", "end-1c"))

    def show_login_screen(self):
        # Mostra novamente a tela de login
        self.root.deiconify()

Login()
