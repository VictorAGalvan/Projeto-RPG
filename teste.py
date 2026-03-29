
from missao import Missao
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao
from missao_combate import MissaoCombate
from status import status_missao


try:
    coleta = MissaoColeta("Coletar", "Coletar moedas",10,"moeda de ouro",5)
    coleta.iniciar_missao()
    coleta.concluir_missao()
    coleta.exibir_dados()
except Exception as e:
    print(f"Erro na MissaoColeta: {e}")


try:
    exploracao = MissaoExploracao("Explorar", "Explorar um vale",30,"Vale",25.5,10)
    exploracao.iniciar_missao()
    exploracao.concluir_missao()
    exploracao.exibir_dados()
except Exception as e:
    print(f"Erro na MissaoExploracao: {e}")

# Teste para Missao_Combate
try:
    combate = MissaoCombate("Matar o dragao", "Matar o dragao de gelo",50,"Dragão de gelo", 1)
    combate.iniciar_missao()
    combate.concluir_missao()
    combate.exibir_dados()
except Exception as e:
    print(f"Erro na Missao_Combate: {e}")
