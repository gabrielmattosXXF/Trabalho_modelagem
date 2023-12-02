class Ficha:
    def __init__(self, nome_ficha):
        self.nome_ficha = nome_ficha
        self.exercicios = {} 
        # abre uma tela para adicionar um exercício. Quando todas as informações do exercício forem preenchidas,
        # o exercício é adicionado ao dicionário de exercícios da ficha

    def adicionar_exercicio(self):
        # abre uma tela para adicionar um exercício. Quando todas as informações do exercício forem preenchidas,
        exercicio = Exercicio()
        ##quando o exercicio é criado pela tela, ele é construido pelo Exrcicio() e adicionado ao dicionário de exercícios
        self.exercicios[exercicio.nome] = exercicio