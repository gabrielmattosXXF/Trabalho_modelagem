class Exercicio:
    def __init__(self, nome, carga, repeticoes, series, comentario):
        self.nome = nome
        self.carga = carga
        self.repeticoes = repeticoes
        self.series = series
        self.comentario = comentario

    def atualizarExercicio(self, nome=None, carga=None, repeticoes=None, series=None): ##none permite que o usuario possa não alterar todas os atributos do problema e so alguns especificos que ele deseja.
        if nome is not None:
            self.nome = nome
        if carga is not None:
            self.carga = carga
        if repeticoes is not None:
            self.repeticoes = repeticoes
        if series is not None:
            self.series = series

    ##Ex: exercicio.atualiza(carga=60, repeticao = None, series = 4, comentario = None)

    def __toString__(self):
        return f"Exercício: {self.nome}\nCarga: {self.carga} kg\nRepetições: {self.repeticoes}\nSéries: {self.series}\nComentário: {self.comentario}" ##toString

    ##def criarExercicio(self, nome, carga, repeticoes, series, comentario):
    ##    self.nome = nome
    ##    self.carga = carga
    ##    self.repeticoes = repeticoes
    ##    self.series = series
    ##    self.comentario = comentario

