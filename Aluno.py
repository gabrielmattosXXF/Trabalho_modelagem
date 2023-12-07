from Usuario import Usuario

class Aluno(Usuario):
    def __init__(self, usuario_pai, Personal,treino):
        super().__init__(usuario_pai.nome, usuario_pai.email, usuario_pai.senha, usuario_pai.CPF, usuario_pai.idade, usuario_pai.telefone, usuario_pai.id_usuario, usuario_pai.tipo_usuario)
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