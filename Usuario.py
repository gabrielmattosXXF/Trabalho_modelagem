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