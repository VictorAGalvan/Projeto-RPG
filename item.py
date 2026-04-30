from exception_geral import ExceptionGeral
from tipo_item import tipoItem
class Item():
    def __init__(self,nome:str, descricao:str,  atributo:int, tipo:str):
        self.nome = nome 
        self.descricao =  descricao
        self.atributo = atributo
        self.tipo = tipo
@property
def nome(self):
    return self.__nome
@property
def descricao(self):
    return self.__descricao
@property
def atributo(self):
    return self.__atributo
@property
def tipo(self):
    return self.__tipo
@nome.setter
def nome(self,nome:str):
    self.__nome = nome
@descricao.setter
def descricao(self,descricao:str):
    self.__descricao = descricao
@atributo.setter
def atriibuto(self,atributo:int):
    self.__atributo = atributo
@tipo.setter
def tipo(self,tipo:str):
    if not tipo in tipoItem:
        raise ExceptionGeral("Tipo não compativel")
    self.__tipo = tipo