
from abc import ABC, abstractmethod

from exceptions.exception_geral import ExceptionGeral
class EstadoMissao(ABC):
    def __init__(self,missao):
        self.missao = missao
    @abstractmethod
    def iniciar(self):
        """inicia a missão"""
        pass
    @abstractmethod
    def concluir(self,valor):
        pass

class EstadoPendente(EstadoMissao):
    def iniciar(self):
        self.missao.status = EstadoAndamento(self.missao)
    def concluir(self,valor=False):
        raise ExceptionGeral("Estado Pendente não pode ser concluido!")
    def __str__(self):
        return "Pendente"
class EstadoAndamento(EstadoMissao):
    def iniciar(self):
        raise ExceptionGeral("Estado Andamento não pode ser Iniciado!")
    def concluir(self,valor):
        if valor:
            self.missao.status = EstadoConcluida(self.missao)
        else:
            self.missao.status = EstadoFracassada(self.missao)
    def __str__(self):
        return "Andamento"

class EstadoConcluida(EstadoMissao):
    def iniciar(self):
        raise ExceptionGeral("Estado Concluido não pode ser modificado!")
    def concluir(self,valor = False):
        raise ExceptionGeral("Estado Concluido não pode ser modificado!")
    def __str__(self):
        return "Concluida"
        
class EstadoFracassada(EstadoMissao):
    def iniciar(self):
        raise ExceptionGeral("Estado Fracassada não pode ser modificado!")
    def concluir(self,valor = False):
        raise ExceptionGeral("Estado Fracassada não pode ser modificado!")
    def __str__(self):
        return "Fracassada"