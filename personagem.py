class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__missoes = []

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
    
    def add_missao(self, nova_missao):
        for m in self.__missoes:
            if(m == nova_missao):
                raise Exception("Missão já existe na lista")
        
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

    def concluir_missao(self, missao, valor):
        sucesso= missao.concluir_missao(valor)
        if sucesso:
            print(f"Missão concluída com sucesso recebendo recompensa de: {missao.recompensa}")
            self.__xp += missao.recompensa
        else:
            print(f"Missão não conseguiu ser concluida com sucesso!")