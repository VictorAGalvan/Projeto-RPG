class Inimigo():
    def __init__(self,nome,vida,ataque):
        self.__nome = nome
        self.__vida= vida
        self.__ataque= ataque
    @property
    def vida(self):
        return self.__vida

    @property
    def ataque(self):
        return self.__ataque
    
    @property
    def nome(self):
        return self.__nome
    @vida.setter
    def vida(self,nova_vida):
        self.__vida = nova_vida
    @ataque.setter
    def ataque(self,ataque):
        self.__ataque = ataque   
    @nome.setter
    def nome(self,nome):
        self.__nome = nome  
    def __eq__(self, value):
        if(self.nome == value.nom and self.vida == value.vida and self.ataque == value.ataque):
            return True
        return False
    def __str__(self):
        return f"\n--------------\nNome: {self.nome}\nAtaque: {self.ataque}\nVida: {self.vida}\n--------------\n"