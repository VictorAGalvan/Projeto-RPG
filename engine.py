from missao import Missao
from personagem import Personagem


class Engine():
    def __init__(self, missao:Missao, personagem:Personagem):
        self.__missao = missao
        self.__personagem = personagem
    def comecar(self):
        