from missao import Missao
class MissaoCombate(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:int, tipo_inimigo:str, inimigos_a_derrotar:int):
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar
        super().__init__(nome, descricao, recompensa)
    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo
    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    @tipo_inimigo.setter
    def tipo_inimigo(self,tipo_inimigo:str):
        if (tipo_inimigo.__class__ != str):
            raise Exception("Tipo de inimigo inválido")
        self.__tipo_inimigo = tipo_inimigo  
    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self,inimigos_a_derrotar:int):
        if (inimigos_a_derrotar.__class__ != int):
            raise Exception("Tipo de inimigo inválido")
        self.__inimigos_a_derrotar = inimigos_a_derrotar 
    def __str__(self):
        tamanho = len(self.nome)
        text = super().__str__()  
        return f"{text} \nTipo de inimigo: {self.tipo_inimigo} \nInimigos a derrotar: {self.inimigos_a_derrotar}"
    

    def __eq__(self, v):
        if  super().__eq__(v) and self.tipo_inimigo == v.tipo_inimigo and self.inimigos_a_derrotar == v.inimigos_a_derrotar:
            return True
        
        return False
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Tipo de inimigo: {self.tipo_inimigo}")
        print(f"Inimigos a derrotar: {self.inimigos_a_derrotar}")

    def concluir_missao(self, inimigos:int):
        if (inimigos.__class__ != int):
            raise Exception("Inimigos tem que ser um inteiro")
        if (inimigos >= self.__inimigos_a_derrotar):
            super().concluir_missao()
            return True
        else:
            return False