from status import status_missao
class Missao:
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
        novo_status = novo_status.strip().upper()
        if (novo_status not in status_missao):
            raise Exception(F"Status tem que ser {status_missao.PENDENTE.value } , {status_missao.EM_ANDAMENTO.value } ou {status_missao.CONCLUIDA.value } ou {status_missao.FRACASSADA.value}")
        index = 0

        fluxo = [status_missao.PENDENTE.value, status_missao.EM_ANDAMENTO.value, [status_missao.CONCLUIDA.value,status_missao.FRACASSADA.value]]
        for i in len(fluxo) :
            if (fluxo[i] == self.status):
                index = i
                break
        if (self.status in fluxo[0:2]):
            if (novo_status != fluxo[index+1]):
                 raise Exception(f"Status atual: {self.__status } (Só pode ser alterado para {fluxo[index+1]})")
        else: 
            if (novo_status != fluxo[3][0] and novo_status != fluxo[3][1]):
                 raise Exception(f"Status atual: {self.__status } (Só pode ser alterado para {fluxo[index+1][0]} ou {fluxo[index+1][1]} )")
       
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
            raise Exception("Missão não é mais pendente e não pode ser alterada!")
    
    def concluir_missao(self):
        if (self.status == status_missao.EM_ANDAMENTO.value):
            self.status = status_missao.CONCLUIDA.value
            print(f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira.")
        else: 
            raise Exception("Missão está em um status que não é EM ANDAMENTO e não pode ser alterada!")