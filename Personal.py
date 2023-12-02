import Usuario

class Personal(Usuario):
    def __init__(self, nome, email, senha, CPF, idade, telefone):
        super().__init__(nome, email, senha, CPF, idade, telefone)
        self.alunos = {}

    def vincularAluno(self, aluno):
        self.alunos[aluno.nome] = aluno ##dicionario com chave sendo nome do aluno, achei implementação mais interessante, visto que nome seria ideial para ID.

    def desligarAluno(self, aluno):
        if aluno.nome in self.alunos:
            self.alunos.pop(aluno.nome) ##remove apenas se existir o aluno

    ##def atribuirTreino(self, aluno, treino):
        ##if aluno.nome in self.alunos:
            ##aluno.setTreino(treino)

    def visualizarAlunos(self):
        print(f"Alunos vinculados ao Personal {self.nome}:")
        for aluno in self.alunos.items():
            print(aluno.get_usuario())