from missao import Missao
class MissaoExploracao(Missao):
    def __init__(self, nome:str, descricao:str, recompensa:str, local:str, distancia_em_km:float,tempo_limite:int):
        self.local = local
        self.distancia = distancia_em_km
        self.tempo_limite = tempo_limite
        super().__init__(nome, descricao, recompensa)
    @property
    def local(self):
        return self.__local
    
    @property
    def distancia(self):
        return self.__distancia
    
    @property
    def tempo_limite(self):
        return self.__tempo_limite

    @local.setter
    def local(self, novo_local:str):
        if (novo_local.__class__ != str):
            raise Exception("Tipo de local inválido")
        self.__local = novo_local
    
    @distancia.setter
    def distancia(self, nova_distancia:float):
        if (nova_distancia.__class__ != float):
            raise Exception("Tipo de quantidade inválido")
        if (nova_distancia < 0 ):
            raise Exception("Valor da distância é negativo")
        self.__distancia = nova_distancia
    @tempo_limite.setter
    def tempo_limite(self, novo_tempo:int):
        if (novo_tempo.__class__ != int):
            raise Exception("Tipo de quantidade inválido")
        if (novo_tempo < 0):
            raise Exception("Valor do tempo é negativo")
        self.__tempo_limite= novo_tempo
        
    def __str__(self):
        text = super().__str__()
        return f"{text} \nLocal: {self.local} \nDistância: {self.distancia} km \nTempo limite: {self.tempo_limite} horas"
    
    def __eq__(self, v):
        if (super().__eq__(v) and 
            self.local == v.local and 
            self.distancia == v.distancia and 
            self.tempo_limite == v.tempo_limite):
            return True
        
        return False
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Local: {self.local}")
        print(f"Distância: {self.distancia} km")
        print(f"Tempo limite: {self.tempo_limite} horas")