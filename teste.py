import time
from personagem import Personagem
from item import Item
from missao_coleta import MissaoColeta
from missao_combate import MissaoCombate
from missao_exploracao import MissaoExploracao
from exception_geral import ExceptionGeral
from fim_de_jogo import FimDeJogo
from tipo_item import Tipo


print("=" * 50)
print(" INICIALIZANDO RPG SEQUENCIAL ".center(50, "="))
print("=" * 50)

try:
   
    nome_usuario = input("Digite o nome do seu Personagem: ")
    jogador = Personagem(nome_usuario)
    print(f"\nBem-vindo, {jogador.nome}!")

    
    espada = Item("Espada de Ferro", "Uma lâmina afiada", 10, Tipo.ARMA.value)
    machado = Item("Machado de Guerra", "Lento mas poderoso", 20, Tipo.ARMA.value)
    armadura = Item("Armadura de Couro", "Proteção básica", 15, Tipo.VESTIMENTA.value)
    placas = Item("Armadura de Placas", "Proteção pesada", 30, Tipo.VESTIMENTA.value)
    escudo = Item("Escudo", "Defesa extra", 5, Tipo.UTILITARIO.value)
    anel = Item("Anel de Vida", "Aumenta vitalidade", 10, Tipo.UTILITARIO.value)

    jogador.add_item(espada)
    jogador.add_item(machado)
    jogador.add_item(armadura)
    jogador.add_item(placas)
    jogador.add_item(escudo)
    jogador.add_item(anel)

    
    print("\n" + "--- SEU INVENTÁRIO ---")
    jogador.mostrar_inventario()

    print("\n[!] Escolha os itens para equipar pelo número:")
    
    inventario = jogador.inventario
    idx_arma = int(input("Número da ARMA: "))
    idx_vest = int(input("Número da VESTIMENTA: "))
    idx_util = int(input("Número do UTILITÁRIO: "))
    jogador.equiparItems(inventario[idx_arma],inventario[idx_vest], inventario[idx_util])
    print("\n[!] Itens iniciais adicionados ao seu inventário.")
    jogador.mostrar_inventario()

    
    print("\n--- EQUIPANDO EQUIPAMENTOS ---")
    jogador
    jogador.equiparItems(espada, armadura, escudo)
    jogador.atualizarAtributos() 
    print("Atributos atualizados com sucesso!")
    jogador.exibir_dados()

    
    print("\n" + "="*10 + " INICIANDO JORNADA DE MISSÕES " + "="*10)

   
    missao1 = MissaoColeta("Ervas do Pântano", "Colete plantas raras", 20, "Planta Verde", 5)
    print(f"\nNova Missão: {missao1.nome}")
    jogador.add_missao(missao1) 
    
    qtd_coletada = int(input(f"Quantas '{missao1.item}' você conseguiu coletar? "))
   
    jogador.concluir_missao(missao1, qtd_coletada)

    print("\n=== PREPARAÇÃO PARA MISSÃO ===")

    jogador.mostrar_inventario()

    inventario = jogador.inventario

    print("\nEscolha os equipamentos:")

    idx_arma = int(input("Número da ARMA: "))
    idx_vest = int(input("Número da VESTIMENTA: "))
    idx_util = int(input("Número do UTILITÁRIO: "))

    jogador.equiparItems(
        inventario[idx_arma],
        inventario[idx_vest],
        inventario[idx_util]
    )

    print("\nSTATUS ATUAL")
    print(f"Ataque: {jogador.ataque}")
    print(f"Vida: {jogador.vida}")
    missao2 = MissaoExploracao("Mapear Deserto", "Explore as dunas", 30, "Deserto de Sal", 50.0, 10)
    print(f"\nNova Missão: {missao2.nome}")
    jogador.add_missao(missao2)

    dist = float(input(f"Qual a distância percorrida em {missao2.local} (km)? "))
    tempo = int(input("Em quanto tempo (horas)? "))
    jogador.concluir_missao(missao2, [dist, tempo])

    print("\n=== PREPARAÇÃO PARA MISSÃO ===")

    jogador.mostrar_inventario()

    inventario = jogador.inventario

    print("\nEscolha os equipamentos:")

    idx_arma = int(input("Número da ARMA: "))
    idx_vest = int(input("Número da VESTIMENTA: "))
    idx_util = int(input("Número do UTILITÁRIO: "))

    jogador.equiparItems(
        inventario[idx_arma],
        inventario[idx_vest],
        inventario[idx_util]
    )

    print("\nSTATUS ATUAL")
    print(f"Ataque: {jogador.ataque}")
    print(f"Vida: {jogador.vida}")
    missao3 = MissaoCombate("Cacada de Orcs", "Limpe o acampamento", 40, "Orc", 3)
    print(f"\nNova Missão: {missao3.nome}")
    jogador.add_missao(missao3)

    inimigos = int(input(f"Quantos {missao3.tipo_inimigo}s você derrotou? "))
    jogador.concluir_missao(missao3, inimigos)


    print("\n" + "=" * 50)
    print(" RESUMO DA AVENTURA ".center(50, "="))
    jogador.exibir_dados()

except ExceptionGeral as e:
    print(f"\n[ERRO DE LÓGICA]: {e}")
except FimDeJogo:
    print("\n" + "!" * 50)
    print(" GAME OVER!".center(50, "!"))
    print("!" * 50)
except Exception as e:
    print(f"\n[ERRO INESPERADO]: {e}")

