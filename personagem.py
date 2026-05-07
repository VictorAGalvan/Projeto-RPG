from exception_geral import ExceptionGeral
from item import Item
from missao import Missao
from fim_de_jogo import FimDeJogo
from tipo_item import Tipo
class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__buffVida = 0
        self.__buffAtaque = 0
        self.__ataque = 10
        self.__ataqueBase = 10
        self.__utilitarioEquipado = None
        self.__armaEquipada = None
        self.__vestimentaEquipada = None
        self.__inventario:list[Item] = []
        self.__missoes:list[Missao] = []
        self.atualizarAtributos()

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
    def missoes(self):
        return self.__missoes
    
    @nome.setter
    def nome (self, novo_nome:str):
        if  novo_nome.__class__ != str :
            raise Exception("Nome do Personagem Inválido")
        novo_nome = novo_nome.strip().title()
        if (novo_nome == ""):
            raise Exception("Nome do Personagem Inválido")
        self.__nome = novo_nome
    def add_item(self, item:Item):
        self.__inventario.append(item)
    def remover_item(self, item:Item):
        if item in self.__inventario:
            self.__inventario.remove(item)
        else:
            raise ExceptionGeral("Item não existe no inventário")   
    def desequiparItems(self):
        self.__armaEquipada = None
        self.__utilitarioEquipado = None
        self.__vestimentaEquipada = None      
        self.__vida -= self.__buffVida
        self.__ataque = self.__ataqueBase
        self.__buffVida=0
        self.__buffAtaque = 0
        if(self.__vida <= 0):
            raise FimDeJogo("Fim de Jogo")
        self.atualizarAtributos()
    def atualizarAtributos(self):
        buffA =0 
        # ATAQUE
        ataque_total = self.__ataque
        
        if self.__armaEquipada:
            buffA += self.__armaEquipada.atributo

        # VIDA
        bonus_percentual = 0

        if self.__vestimentaEquipada:
            bonus_percentual += self.__vestimentaEquipada.atributo

        if self.__utilitarioEquipado:
            bonus_percentual += self.__utilitarioEquipado.atributo

        bonus_vida = self.__vida * (bonus_percentual / 100)

        

        vida_total = self.vida + bonus_vida
        # LIMITE MÁXIMO
        if vida_total > 100:
            excedente = vida_total - 100
            bonus_vida -= excedente
            vida_total = 100
        
        self.__buffAtaque = buffA
        self.__buffVida = bonus_vida
        self.__ataque = int(ataque_total)
        self.__vida = int(vida_total)
    def equiparItems(self,arma:Item,vestimenta:Item,utilitario:Item):
        if arma not in self.__inventario:
            raise ExceptionGeral("Arma não está no inventário")
        if vestimenta not in self.__inventario:
            raise ExceptionGeral("Vestimenta não está no inventário")
        if utilitario not in self.__inventario:
            raise ExceptionGeral("Utilitário não está no inventário")
        
        if(arma.tipo != Tipo.ARMA.value ):
            raise ExceptionGeral("Tipo de item inválido para equipar a arma")
        if(vestimenta.tipo != Tipo.VESTIMENTA.value):
            raise ExceptionGeral("Tipo de item inválido para equipar a vestimenta")
        if(utilitario.tipo != Tipo.UTILITARIO.value):
            raise ExceptionGeral("Tipo de item inválido para equipar o utilitario")
        self.__armaEquipada = arma
        self.__vestimentaEquipada = vestimenta
        self.__utilitarioEquipado = utilitario
        self.atualizarAtributos()
    def mostrar_inventario(self):
        cont =0
        print("--------- INVETARIO ---------")
        for i in self.inventario:
            print(f'[{cont}]{i}')
            cont +=1
        print("-----------------------------")
       
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
    def exibir_missoes(self):
        cont =0
        if self.__missoes == None:
            print("Sem missões")
            print("-"*50)
        for m in self.__missoes:
            print(f"[{cont}] - {m}")
            cont +=1
          
        print("-"*50)
        pass
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
        self.desequiparItems()
    def __fracasso_missao(self):
        vida = 50
        print(f"Missão fracassada. Irá perder {vida} pontos de vida!")
        self.__retirar_vida(vida)