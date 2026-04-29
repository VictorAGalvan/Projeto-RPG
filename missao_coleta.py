from missao import Missao
class MissaoColeta(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:int, item:str, quantidade:int):
        self.item = item
        self.quantidade = quantidade
        super().__init__(nome, descricao, recompensa)
    @property
    def item(self):
        return self.__item
    @property
    def quantidade(self):
        return  self.__quantidade
    @item.setter
    def item(self, novo_item:str):
        if (novo_item.__class__ != str):
             raise Exception("Tipo de item inválido")
        self.__item = novo_item
    @quantidade.setter
    def quantidade(self, nova_quantidade:int):
        if (nova_quantidade.__class__ != int):
             raise Exception("Tipo de quantidade inválido")
        self.__quantidade = nova_quantidade
        
    def __str__(self):
        text = super().__str__()
        return f"{text} \nItem: {self.item} \nQuantidade: {self.quantidade}"

    def __eq__(self, v):
        if (super().__eq__(v) and 
            self.item == v.item and 
            self.quantidade == v.quantidade):
            return True
        
        return False

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Item: {self.item}")
        print(f"Quantidade: {self.quantidade}")    
    def concluir_missao(self, quantidade:int):
        if (quantidade.__class__ != int):
            raise Exception("Quantidade tem que ser um inteiro")
        if (quantidade >= self.__quantidade):
            super().concluir_missao()
            return True
        else:
            return False
    