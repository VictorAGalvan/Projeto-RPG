from status import status_missao
class Missao:
    def __init__(self, nome:str, descricao:str, recompensa:int):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.__status = status_missao.PENDENETE.value
    
    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def recompensa(self):
        return self.__recompensa
    @property
    def status(self):
        return self.__status
    
    @nome.setter
    def nome(self, novo_nome:str):
        if novo_nome.__class__ != str:
            raise Exception("Nome da Missão inválido")
        if novo_nome.strip() == "":
             raise Exception("Nome da Missão inválido")
        novo_nome = novo_nome.strip().title()
        self.__nome = novo_nome
    @descricao.setter
    def descricao(self, nova_descricao:str):
        if nova_descricao.__class__ != str:
            raise Exception("Descrição inválida")
        if nova_descricao.strip() == "":
            raise Exception("Descrição inválida")
        nova_descricao = nova_descricao[0].upper() + nova_descricao[1:]
        self.__descricao = nova_descricao
    @recompensa.setter
    def recompensa(self, nova_recompensa:int):
        if (nova_recompensa < 1 or nova_recompensa > 50):
            raise Exception("Recompensa Inválida")
        self.__recompensa = nova_recompensa
    @status.setter
    def status(self, novo_status:str):
        if novo_status.__class__ != str:
            raise Exception("Status Inválido")
        novo_status = novo_status.strip().title()
        if (novo_status != status_missao.EM_ANDAMENTO.value and novo_status != status_missao.EM_ANDAMENTO.value and novo_status != status_missao.CONCLUIDA.value):
            raise Exception(F"Status tem que ser {status_missao.PENDENTE.value } , {status_missao.EM_ANDAMENTO.value } ou {status_missao.CONCLUIDA.value }")
        if (self.__status == status_missao.PENDENTE.value and novo_status != status_missao.EM_ANDAMENTO.value):
            raise Exception(f"Status atual: {self.__status } (Só pode ser alterado para {status_missao.EM_ANDAMENTO.value})")
        if (self.__status == status_missao.EM_ANDAMENTO.value and novo_status != status_missao.CONCLUIDA.value):
            raise Exception(f"Status atual: {self.__status } (Só pode ser alterado para {status_missao.CONCLUIDA.value})")
        if (self.__status == status_missao.CONCLUIDA.value):
            raise Exception(f"Status atual: {self.__status } (A tarefa já foi concluida e não pode mudar) ")


        self.__status = novo_status
    def exibir_dados(self):
        print(f"Nome missão: {self.__nome}")
        print(f"descrição: {self.__descricao}")
        print(f"Recompensa: {str(self.__recompensa)}")
        print(f"Status: {self.__status}")
    def __str__(self):
        tamanho = len(self.__nome)
        text = tamanho * "-" + "\nNome missão: " + self.__nome + "\nDescrição: " + self.__descricao + "\nRecompensa: " + str(self.__recompensa) +  "\nStatus: " + self.__status + "\n" + tamanho * "-" + "\n"
        
        return text


    def __eq__(self, v):
        if self.__nome == v.nome and self.__descricao == v.descricao and self.__recompensa == v.recompensa and self.__status == v.status:
            return True
        
        return False