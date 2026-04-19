from missao import Missao
from missao_coleta import MissaoColeta
from missao_exploracao import MissaoExploracao
from missao_combate import MissaoCombate
from personagem import Personagem
from status import status_missao

p = Personagem("Arthur")

print("========== TESTES DE SUCESSO ==========")

print("\n--- SUCESSO: Coleta ---")
try:
    coleta = MissaoColeta("Coletar", "Coletar moedas", 10, "moeda de ouro", 5)
    p.add_missao(coleta)
    
    p.concluir_missao(coleta, 8)  # suficiente

    coleta.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")


print("\n--- SUCESSO: Exploracao ---")
try:
    exploracao = MissaoExploracao("Explorar", "Explorar um vale", 30, "Vale", 25.5, 10)

    p.add_missao(exploracao)

    # supondo: [distancia, tempo]
    p.concluir_missao(exploracao, [30.0, 8])  # suficiente

    exploracao.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")


print("\n--- SUCESSO: Combate ---")
try:
    combate = MissaoCombate("Matar o dragao", "Matar o dragao de gelo", 50, "Dragão de gelo", 1)

    p.add_missao(combate)
    p.concluir_missao(combate, 1)  # suficiente

    combate.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")
p.exibir_dados()

print("\n========== TESTES DE FALHA ==========")


print("\n--- FALHA: Coleta ---")
try:
    coleta_fail = MissaoColeta("Coletar ervas", "Coletar ervas raras", 15, "erva rara", 10)

    p.add_missao(coleta_fail)
    p.concluir_missao(coleta_fail, 3)  # insuficiente

    coleta_fail.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")


print("\n--- FALHA: Exploracao ---")
try:
    exploracao_fail = MissaoExploracao("Explorar caverna", "Explorar caverna profunda", 20, "Caverna", 50.0, 5)

    p.add_missao(exploracao_fail)

    # distância insuficiente
    p.concluir_missao(exploracao_fail, [30.0, 6])

    exploracao_fail.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")



print("\n--- FALHA: Combate ---")
try:
    combate_fail = MissaoCombate("Cacar lobos", "Cacar lobos selvagens", 25, "Lobo selvagem", 5)

    p.add_missao(combate_fail)
    p.concluir_missao(combate_fail, 2)  # insuficiente

    combate_fail.exibir_dados()
except Exception as e:
    print(f"Erro: {e}")


# =========================
# DADOS FINAIS
# =========================
print("\n========== RESULTADO FINAL ==========")
p.exibir_dados()