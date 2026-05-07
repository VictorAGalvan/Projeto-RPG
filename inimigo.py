class Inimigo():
    def __init__(self,vida,ataque):
        self.__vida= vida
        self.__ataque= ataque
    @property
    def vida(self):
        return self.__vida

    @property
    def ataque(self):
        return self.__ataque
    @vida.setter
    def vida(self,nova_vida):
        self.__vida = nova_vida
    @ataque.setter
    def vida(self,ataque):
        self.__ataque = ataque   
    