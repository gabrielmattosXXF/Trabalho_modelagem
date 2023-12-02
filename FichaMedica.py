class FichaMedica():
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
    def criarFichaMedica(self):
        self.sexo = input("Digite seu sexo: ")
        self.altura = input("Digite sua altura: ")
        self.MassaBranca = input("Digite sua massa branca: ")
        self.percentualGordura = input("Digite seu percentual de gordura: ")
        self.problemasSaude = input("Digite seus problemas de saúde: ")
        self.medicamentosUso = input("Digite os medicamentos que você usa: ")
        self.historicosLesoes = input("Digite seus históricos de lesões: ")
        self.cirurgias = input("Digite suas cirurgias: ")
        self.contatoEmergencia = input("Digite o contato de emergência: ")
        self.telefoneEmergencia = input("Digite o telefone de emergência: ")