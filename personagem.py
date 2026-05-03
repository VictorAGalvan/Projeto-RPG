from exception_geral import ExceptionGeral
from item import Item
from missao import Missao
from fim_de_jogo import FimDeJogo
from tipo_item import tipoItem
class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__buffVida = 0
        self.__ataque = 1
        self.__buffAtaque = 0
        self.__utilitarioEquipado = None
        self.__armaEquipada = None
        self.__vestimentaEquipada = None
        self.__inventario:list[Item] = []
        self.__missoes:list[Missao] = []

    @property
    def buffVida(self):
        return self.__buffVida
    @property
    def buffAtaque(self):
        return self.__buffAtaque
    @property
    def utilitarioEquipado(self):
        return self.__utilitarioEquipado

    @property
    def armaEquipada(self):
        return self.__armaEquipada
    
    @property
    def vestimentaEquipada(self):
        return self.__vestimentaEquipada

    @property
    def inventario(self):
        return self.__inventario
    @property
    def ataque(self):
        return self.__ataque
    @property
    def nome(self) -> str:
        return self.__nome
    @property
    def nivel(self):
        return self.__nivel
    @property
    def xp(self):
        return self.__xp
    @property
    def vida(self):
        return self.__vida
    @property
    def missao(self):
        return self.__missao
    
    @nome.setter
    def nome (self, novo_nome:str):
        if  novo_nome.__class__ != str :
            raise Exception("Nome do Personagem Inválido")
        novo_nome = novo_nome.strip().title()
        if (novo_nome == ""):
            raise Exception("Nome do Personagem Inválido")
        self.__nome = novo_nome
    
    def remover_item(self, item:Item):
        if item in self.__inventario:
            self.__inventario.remove(Item)
        else:
            raise ExceptionGeral("Item não existe no inventário")
    
    def desequiparItems(self):
        self.__armaEquipada = None
        self.__utilitarioEquipado = None
        self.__vestimentaEquipada = None

        
    def atualizarAtributos(self):
        self.__buffVida += self.vestimentaEquipada.atributo
        self.__buffVida += self.utilitarioEquipado.atributo
        self.__buffAtaque += self.armaEquipada.atributo

        if(self.vida + self.buffVida > 100):
            self.__buffVida = self.vida + self.buffVida - 100
        self.__vida += self.buffVida
        self.__ataque += self.buffAtaque
    def equiparItems(self,arma:Item,vestimenta:Item,utilitario:Item):
        if(arma.tipo != tipoItem.ARMA.value ):
            raise ExceptionGeral("Tipo de item inválido para equipar a arma")
        if(vestimenta.tipo != tipoItem.VESTIMENTA.value):
            raise ExceptionGeral("Tipo de item inválido para equipar a vestimenta")
        if(utilitario.tipo != tipoItem.UTILITARIO.value):
            raise ExceptionGeral("Tipo de item inválido para equipar o utilitario")
        self.__armaEquipada = arma
        self.__vestimentaEquipada = vestimenta
        self.__utilitarioEquipado = utilitario


    def mostrar_inventario(self):
        pass
    def add_xp(self,valor:int):
        self.__xp += valor        
        while self.__xp >=100:
            self.__xp -=100
            self.__nivel +=1


    def add_missao(self, nova_missao):
        for m in self.__missoes:
            if(m == nova_missao):
                raise ExceptionGeral("Missão já existe na lista")
        
        nova_missao.iniciar_missao() 
        self.__missoes.append(nova_missao)

    def __str__(self):
        tamanho = len(self.nome)
        text = tamanho* "-" + "\nNome: " + self.__nome + "\nNivel: " + str(self.__nivel) + "\nXP: " + str(self.__xp) + "\nVida: " + str(self.__vida) + "\n" + tamanho * "-" + "\n"
        return text
    def __eq__(self, v):
        if self.__nome == v.nome and self.__nivel == v.nivel and self.__xp == v.xp and self.__vida == v.vida:
            return True
    
        return False
    def exibir_dados(self): 
        tamanho = len(self.nome)
        texto = tamanho* "-" + "\nNome: " + self.__nome + "\nNivel: " + str(self.__nivel) + "\nXP: " + str(self.__xp) + "\nVida: " + str(self.__vida) + "\n" + tamanho * "-" + "\n"
        print(texto)
        if (len(self.__missoes) > 0 ):
            for m in self.__missoes:
                print(m)
        else:
            print("Não tem missões")
    def __retirar_vida(self, valor:int):
        if(valor.__class__ != int):
            raise ExceptionGeral("Valor para retirar a vida é diferente de inteiro")
        if(valor <= 0):
            raise ExceptionGeral("Valor Inválido. Valor para retirar a vida tem que ser maior que 0!")
        self.__vida -= valor
        if(self.__vida <=0):
            self.__vida = 0
            print ("Fim de Jogo!")
            self.exibir_dados()
            raise FimDeJogo("")

    def concluir_missao(self, missao, valor):
        sucesso= missao.concluir_missao(valor)
        #print(sucesso)
        if sucesso:
            print(f"Missão concluída com sucesso recebendo recompensa de: {missao.recompensa}")
            self.add_xp(missao.recompensa)
            self.__retirar_vida(1)
        else:
            self.__fracasso_missao()
            print(f"Missão não conseguiu ser concluida com sucesso!")
    def __fracasso_missao(self):
        vida = 50
        print(f"Missão fracassada. Irá perder {vida} pontos de vida!")
        self.__retirar_vida(vida)