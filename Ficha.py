from Exercicio import Exercicio
import json

class Ficha:
    def __init__(self, nome_ficha):
        self.nome_ficha = nome_ficha
        self.exercicios = {} 
        # abre uma tela para adicionar um exercício. Quando todas as informações do exercício forem preenchidas,
        # o exercício é adicionado ao dicionário de exercícios da ficha

    def adicionar_exercicio(self, nome, carga, repeticoes, serie, comentario):
        exercicio = Exercicio(nome, carga, repeticoes, serie, comentario)
        self.exercicios[exercicio.nome] = exercicio

    def to_json(self):
        return json.dumps({"nome_ficha": self.nome_ficha, "exercicios": self.exercicios}, indent=2)

    def salvar_para_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({"nome_ficha": self.nome_ficha, "exercicios": self.exercicios}, file, indent=2)