""" from tkinter import Tk, Label, Button, Frame
from Ficha import Ficha
from view_ficha import view_ficha

class view_treino:
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.create_widgets()
        self.root.mainloop()

    def screen(self):
        cor_de_fundo = "#D2E3FC"
        fonte_titulo = ("Helvetica", 18, "bold")

        largura_janela = 600
        altura_janela = 400

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x_pos = (largura_tela - largura_janela) // 2
        y_pos = (altura_tela - altura_janela) // 2

        self.root.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")
        self.root.title("Ficha médica")
        self.root.configure(bg=cor_de_fundo)

    def exibir_ficha(self, ficha):
        view_ficha_instance = view_ficha(ficha)
        # Não chame mainloop aqui

    def create_widgets(self):
        cor_de_fundo = "#D2E3FC"
        fonte_titulo = ("Helvetica", 18, "bold")
        fonte_texto = ("Helvetica", 12)

        frame = Frame(self.root, bg=cor_de_fundo)
        frame.pack(expand=True, fill="both", pady=20, padx=20)

        Label(frame, text="Treinos", font=fonte_titulo, bg=cor_de_fundo).grid(row=0, column=0, pady=(0, 20))

        ficha1 = Ficha("Ficha 1")
        ficha1.adicionar_exercicio("Supino", 50, 10, 3, "Comentário 1")
        ficha1.adicionar_exercicio("Rosca direta", 10, 10, 3, "Comentário 2")
        ficha2 = Ficha("Ficha 2")
        ficha2.adicionar_exercicio("Triceps", 10, 10, 3, "Comentário 3")
        ficha2.adicionar_exercicio("Supina", 50, 10, 3, "Comentário 1")
        ficha3 = Ficha("Ficha 3")
        ficha3.adicionar_exercicio("Rosca adentro", 10, 10, 3, "Comentário 2")
        ficha3.adicionar_exercicio("Tripas", 10, 10, 3, "Comentário 3")

        Button(frame, text="Ficha 1", command=lambda: self.exibir_ficha(ficha1), font=fonte_texto, bg="#4CAF50", fg="white", padx=20, pady=10).grid(row=1, column=0, pady=10)
        Button(frame, text="Ficha 2", command=lambda: self.exibir_ficha(ficha2), font=fonte_texto, bg="#1976D2", fg="white", padx=20, pady=10).grid(row=2, column=0, pady=10)
        Button(frame, text="Ficha 3", command=lambda: self.exibir_ficha(ficha3), font=fonte_texto, bg="#FF5722", fg="white", padx=20, pady=10).grid(row=3, column=0, pady=10)

        for child in frame.winfo_children():
            child.grid_configure(pady=(10, 10))

# Executa o aplicativo
view_treino()
 """

from tkinter import Tk, Label, Button, Frame
from Ficha import Ficha
from view_ficha import view_ficha

class view_treino:

    def __init__(self):
        self.root = Tk()
        self.root.title("Seleção de Treino")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        cor_de_fundo = "#f0f0f0"
        fonte = ("Helvetica", 12)

        Label(self.root, text="Escolha sua ficha", font=("Helvetica", 16), bg=cor_de_fundo).pack(pady=20)

        # Simulando 3 fichas com exercícios preenchidos
        ficha1 = Ficha("Peito e triceps")
        ficha1.adicionar_exercicio("Supino", 50, 10, 3, "Comentário 1")
        ficha1.adicionar_exercicio("Rosca direta", 10, 10, 3, "Comentário 2")
        ficha1.adicionar_exercicio("Tríceps", 10, 10, 3, "Comentário 3")

        ficha2 = Ficha("Costas e biceps")
        ficha2.adicionar_exercicio("Agachamento", 80, 8, 4, "Comentário 4")
        ficha2.adicionar_exercicio("Levantamento Terra", 100, 6, 3, "Comentário 5")
        ficha2.adicionar_exercicio("Flexão", 0, 15, 3, "Comentário 6")

        ficha3 = Ficha("Perna e ombro")
        ficha3.adicionar_exercicio("Corrida", 0, 0, 1, "Comentário 7")
        ficha3.adicionar_exercicio("Natação", 0, 0, 1, "Comentário 8")
        ficha3.adicionar_exercicio("Ciclismo", 0, 0, 1, "Comentário 9")

        fichas = [ficha1, ficha2, ficha3]

        for i, ficha in enumerate(fichas, start=1):
            button_text = f"Ficha {i}: {ficha.nome_ficha}"
            Button(self.root, text=button_text, command=lambda f=ficha: self.show_ficha_details(f), font=fonte, bg="#4CAF50", fg="white").pack(pady=10)

    def show_ficha_details(self, ficha):
        self.root.withdraw()  # Esconde a tela atual
        view_ficha(ficha)  # Mostra a tela de detalhes da ficha

if __name__ == "__main__":
    view_treino()