from models.missao_coleta import MissaoColeta
from models.missao_combate import MissaoCombate
from models.missao_exploracao import MissaoExploracao
class FactoryMissao():
    @staticmethod
    def criar_missao(tipo_missao:str, nome ,descricao, recompensa, **kwargs):
        missao = None
        if tipo_missao == "combate":
            missao = MissaoCombate(nome, descricao,recompensa,kwargs.get("tipo_inimigo"),kwargs.get("quantidade"))
        elif tipo_missao =="coleta":
            missao = MissaoColeta(nome,descricao,recompensa,kwargs.get("item"),kwargs.get("quantidade"))
        elif tipo_missao == "exploracao":
            missao = MissaoExploracao(nome,descricao,recompensa,kwargs.get("local"),kwargs.get("distancia"),kwargs.get("tempo_limite"))
        return missao