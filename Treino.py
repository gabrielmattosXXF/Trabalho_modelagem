from Exercicio import Exercicio
from Ficha import Ficha

class Treino:
    def __init__(self, dataInicio, dataFinal):
        self.Ficha = {}
        self.dataInicio = dataInicio
        self.dataFinal = dataFinal
        self.atual = True

    def criaFicha(self, nome_ficha, exercicios):
        nova_ficha = Ficha(nome_ficha)
        for nome_exercicio, carga, repeticoes, series, comentario in exercicios:
            novo_exercicio = Exercicio(nome_exercicio, carga, repeticoes, series, comentario)
            nova_ficha.adicionar_exercicio(novo_exercicio)
        self.fichas[nome_ficha] = nova_ficha

    def removeFicha(self, nome_ficha):
        if nome_ficha in self.fichas:
            self.fichas.pop(nome_ficha)

    def montaTreino(self):
        print(f"Treino do {self.dataInicio} até {self.dataFinal}")
        for ficha in self.fichas.items():
            ficha.montaFicha()
            print("===")
        