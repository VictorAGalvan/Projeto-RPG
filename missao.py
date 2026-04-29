from status import status_missao
from abc import ABC
from exception_geral import ExceptionGeral
class Missao(ABC):
    def __init__(self, nome:str, descricao:str, recompensa:int):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.__status = status_missao.PENDENTE.value
    
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
            raise ExceptionGeral("Nome da Missão inválido")
        if novo_nome.strip() == "":
             raise ExceptionGeral("Nome da Missão inválido")
        novo_nome = novo_nome.strip().title()
        self.__nome = novo_nome
    @descricao.setter
    def descricao(self, nova_descricao:str):
        if nova_descricao.__class__ != str:
            raise ExceptionGeral("Descrição inválida")
        if nova_descricao.strip() == "":
            raise ExceptionGeral("Descrição inválida")
        nova_descricao = nova_descricao[0].upper() + nova_descricao[1:]
        self.__descricao = nova_descricao
    @recompensa.setter
    def recompensa(self, nova_recompensa:int):
        if (nova_recompensa < 1 or nova_recompensa > 50):
            raise ExceptionGeral("Recompensa Inválida")
        self.__recompensa = nova_recompensa
    @status.setter
    def status(self, novo_status:str):
        if novo_status.__class__ != str:
            raise ExceptionGeral("Status Inválido")
        novo_status = novo_status.strip().upper()
        
        status_validos = [status_missao.PENDENTE.value, status_missao.EM_ANDAMENTO.value, 
                         status_missao.CONCLUIDA.value, status_missao.FRACASSADA.value]
        if novo_status not in status_validos:
            raise ExceptionGeral(f"Status tem que ser {status_missao.PENDENTE.value}, {status_missao.EM_ANDAMENTO.value}, {status_missao.CONCLUIDA.value} ou {status_missao.FRACASSADA.value}")
        
        if self.__status == status_missao.PENDENTE.value:
            if novo_status != status_missao.EM_ANDAMENTO.value:
                raise ExceptionGeral(f"Status atual: {self.__status} (Só pode ser alterado para {status_missao.EM_ANDAMENTO.value})")
        
        elif self.__status == status_missao.EM_ANDAMENTO.value:
            if novo_status != status_missao.CONCLUIDA.value and novo_status != status_missao.FRACASSADA.value:
                raise ExceptionGeral(f"Status atual: {self.__status} (Só pode ser alterado para {status_missao.CONCLUIDA.value} ou {status_missao.FRACASSADA.value})")
        
        elif self.__status == status_missao.CONCLUIDA.value or self.__status == status_missao.FRACASSADA.value:
            raise ExceptionGeral(f"Status atual: {self.__status} (Missão finalizada, não pode ser alterada)")
        
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
    
    def iniciar_missao(self):
        if (self.status == status_missao.PENDENTE.value):
            self.status = status_missao.EM_ANDAMENTO.value
            print(f"A missão {self.nome} começou! Objetivo central da missão: {self.descricao}")
        else:
            raise ExceptionGeral("Missão não é mais pendente e não pode ser alterada!")
    
    def _concluir_missao(self):
        if (self.status == status_missao.EM_ANDAMENTO.value):
            self.status = status_missao.CONCLUIDA.value
            print(f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
            return True
        else: 
            raise ExceptionGeral("Missão está em um status que não é EM ANDAMENTO e não pode ser alterada!")
    def _fracasso_missao(self):
        if (self.status == status_missao.EM_ANDAMENTO.value):
            self.status = status_missao.FRACASSADA.value
            
            return True
        else: 
            raise ExceptionGeral("Missão está em um status que não é EM ANDAMENTO e não pode ser alterada!")