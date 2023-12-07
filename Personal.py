import Usuario

class Personal(Usuario):
    def __init__(self, usuario_pai):
        super().__init__(usuario_pai.nome, usuario_pai.email, usuario_pai.senha, usuario_pai.CPF, usuario_pai.idade, usuario_pai.telefone, usuario_pai.id_usuario, usuario_pai.tipo_usuario)
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