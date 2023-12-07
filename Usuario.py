class Usuario:
    def __init__(self, nome, email, senha, CPF, idade, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.CPF = CPF
        self.idade = idade
        self.telefone = telefone

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def get_CPF(self):
        return self.CPF

    def get_idade(self):
        return self.idade

    def get_telefone(self):
        return self.telefone

    def set_nome(self, nome):
        self.nome = nome

    def set_email(self, email):
        self.email = email

    def set_senha(self, senha):
        self.senha = senha

    def set_CPF(self, CPF):
        self.CPF = CPF

    def set_idade(self, idade):
        self.idade = idade

    def set_telefone(self, telefone):
        self.telefone = telefone


    def RecuperarSenha(self):
        pass

    def FazerLogin(self):
        pass
    
    def FazerLogout(self):
        pass

    def EditarPerfil(self):
        pass

    def VisualizarMeuPerfil(self):
        pass

    def VisualizarNotificações(self):
        pass

    import Usuario

class Aluno(Usuario):
    def __init__(self,Personal,treino):
        super().__init__(Personal,treino)
        self.Personal = None
        self.treino = treino
        self.FichaMedica = None

    def set_Personal(self,Personal):
        self.Personal = Personal

    def set_treino(self,treino):
        self.treino = treino

    def DesligarPersonal(self):
        self.Personal = None

    def ComentarPersonal(self):
        pass

    def VisualizarProgresso(self):
        pass

    def AdicionarFichaMedica(self,FichaMedica):
        self.FichaMedica = FichaMedica    

    def VisualizarTreino(self):
        pass

    def VisualizarFichaMedica(self):
        pass


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