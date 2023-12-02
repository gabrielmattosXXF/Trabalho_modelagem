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