from personagem import Personagem
from item import Item
from missao import Missao
from missao_coleta import MissaoColeta
from missao_combate import MissaoCombate
from missao_exploracao import MissaoExploracao
from exception_geral import ExceptionGeral
from fim_de_jogo import FimDeJogo
from tipo_item import Tipo


missoes:list[Missao] =[]

print("=" * 50)
print(" INICIALIZANDO RPG SEQUENCIAL ".center(50, "="))
print("=" * 50)

try:
    nome_usuario = input("Digite o nome do seu Personagem: ")
    jogador = Personagem(nome_usuario)
    print(f"\nBem-vindo, {jogador.nome}!")
    while True:

        print(f"----Menu----")
        print(f"0 - Sair")
        print(f"1 - Digitar missão")
        print(f"2 - Digitar item")
        print(f"3 - Adicionar missão no personagem: ")
        print(f"4 - Concluir missão")
        print(f"5 - Ver Inventário")
        print(f"6 - Ver personagem")
        print(f"7 - DEBUG")
        opc = int(input("Digite a opção"))
        match opc:
            case 1:
                print("Tipo de missões: ")
                print("1 - Missao Coleta")
                print("2 - Missao Aventura") 
                print("3 - Missao Combate") 
                opc2 = int(input ("Digite o tipo: "))
                nome = input("Digite o nome da missão:")
                desc = input("Digite a descrição da missão:")
                recompensa = int(input("Digite a recompensa da missão:"))

                match opc2:
                    case 1:
                        item_coleta = input("Digite o item a ser coletado: ")
                        quantidade = int(input("Quantidade de items: "))
                        missoes.append(MissaoColeta(nome,desc,recompensa,item_coleta,quantidade))
                    case 2:
                        local = input("Digite o local: ")
                        distancia = float(input("Digite a distancia: "))
                        tempo = int(input("Digite o tempo limite em horas: "))
                        missoes.append(MissaoExploracao(nome,desc,recompensa,local,distancia,tempo))
                    case 3: 
                        inimigo = input("Digite o inimigo: ")
                        quantidade = int(input("Digite a quantidade de inimigos: "))
                        missoes.append(MissaoCombate(nome,desc,recompensa,inimigo,quantidade))
                    case _:
                        print("Error opção inválida")

            case 2:
                tipo = input("Digite o tipo de Item (ARMA, VESTIMENTA, UTILITARIO): ")
                if not tipo in Tipo:
                    print("Tipo não existe")
                nome = input("Digite o nome do item: " )
                desc = input("Digite a descrição do item: ")
                atributo = int(input("Digite o percentual que o item tem de atributo: "))
                jogador.add_item(Item(nome,desc,atributo,tipo))
            case 3:
                cont =0
                for m in missoes:
                    print(f"[{cont}] - {m}")
                    cont += 1
                idx = int(input("Digite qual missão quer adicionar no personagem: "))
                jogador.add_missao(missoes[idx])
            case 4:
                print("\n" + "--- SEU INVENTÁRIO ---")
                jogador.mostrar_inventario()
                print("Deseja equipar algo? 0 para não e 1 para sim")
                opc2 = int(input("Digite:"))
                if(opc2 == 1):
                    print("\n[!] Escolha os itens para equipar pelo número:")
                    
                    inventario = jogador.inventario
                    idx_arma = int(input("Número da ARMA: "))
                    idx_vest = int(input("Número da VESTIMENTA: "))
                    idx_util = int(input("Número do UTILITÁRIO: "))
                    if idx_arma == -1:
                        arma = Item("Nenhum", "none", Tipo.ARMA.value )
                    else:
                        arma = inventario[idx_arma]
                    if idx_vest == -1:
                        vest = Item("Nenhum", "none", Tipo.VESTIMENTA.value )
                    else:
                        vest = inventario[idx_vest]
                    if idx_util == -1:
                        util =  Item("Nenhum", "none", Tipo.UTILITARIO.value )
                    else:
                        util = inventario[idx_util]
                    
                                    
                    jogador.equiparItems(arma,vest,util)
                    print("Itens Equipados!")
                    #jogador.mostrar_inventario()
                
                print("-"*50)
                jogador.exibir_missoes()
                opc2 = int(input("Digite qual missão deseja concluir: "))
                missao = jogador.missoes[opc2]
                if(missao.__class__ == MissaoColeta):
                    qtd_coletada = int(input(f"Quantas '{jogador.missoes[opc2].item}' você conseguiu coletar? "))
                    jogador.concluir_missao(jogador.missoes()[opc2], qtd_coletada)
                elif missao.__class__ == MissaoCombate:
                    inimigos = int(input(f"Quantos {missao.tipo_inimigo}s você derrotou? "))
                    jogador.concluir_missao(missao, inimigos)
                elif missao.__class__ == MissaoExploracao:
                    dist = float(input(f"Qual a distância percorrida em {missao.local} (km)? "))
                    tempo = int(input("Em quanto tempo (horas)? "))
                    jogador.concluir_missao(missao, [dist, tempo])
            case 5:
                jogador.mostrar_inventario()
            case 6:
                print(jogador)
            case 7:
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

