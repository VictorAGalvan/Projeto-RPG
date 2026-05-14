import random

from inimigo import Inimigo
from missao import Missao
from missao_coleta import MissaoColeta
from missao_combate import MissaoCombate
from missao_exploracao import MissaoExploracao
from personagem import Personagem

#p= Personagem("victor")
#m = MissaoCombate("matar goblin","matar",10,Inimigo("goblin",25,1),3)

class Engine():
    def __init__(self, missao:Missao, personagem:Personagem):
        self.__missao = missao
        self.__personagem = personagem
    @property
    def missao(self):
        return self.__missao
    def comecar(self):
        if (self.__missao.__class__ == MissaoExploracao):
            return self.missao_ex()
        elif(self.__missao.__class__ == MissaoCombate):
            return self.missao_co()
        elif(self.__missao.__class__ == MissaoColeta):
            return self.missao_col()

    def missao_ex(self):
        print("-" * 50)
 
        distancia_alvo = self.__missao.distancia
        tempo_limite   = self.__missao.tempo_limite
        velocidade     = self.__personagem.velocidade   # km por hora
 
        distancia_percorrida = 0.0
        hora = 1
 
        print(f"Objetivo: percorrer {distancia_alvo} km em até {tempo_limite} h")
        print(f"Velocidade do personagem: {velocidade} km/h")
        print("----")
 
        while hora <= tempo_limite and distancia_percorrida < distancia_alvo:
 
            print(f"HORA {hora}")
 
           
            fator = random.uniform(0.6, 1.0)
            km_rodada = round(velocidade * fator, 2)
            distancia_percorrida = round(distancia_percorrida + km_rodada, 2)
 
            print(f"Terreno (fator {fator:.2f}): percorreu {km_rodada} km nesta hora")
            print(f"Distância acumulada: {distancia_percorrida} / {distancia_alvo} km")
 
            
            desgaste = max(1, int(10 / velocidade * 2))
            self.__personagem.retirar_vida(desgaste)
            print(f"Desgaste físico: -{desgaste} de vida  |  Vida atual: {self.__personagem.vida}")
            print("----")
 
            hora += 1
 
        if distancia_percorrida >= distancia_alvo and self.__personagem.vida > 0:
            print(f"Exploração concluída! {distancia_percorrida} km percorridos em {hora - 1} h.")
            return True
 
        print(f"Exploração fracassada. Percorreu {distancia_percorrida} km de {distancia_alvo} km necessários.")
        return False
  
    def missao_co(self):
        print("-" * 50)

        cont = 1
        quantidade = self.__missao.inimigos_a_derrotar

        
        base = self.__missao.tipo_inimigo

        while quantidade > 0 and self.__personagem.vida > 0:

            print(f"ROUND {cont}")
            print("----")

            
            inimigo = Inimigo(
                base.nome,
                base.vida,
                base.ataque
            )

            while inimigo.vida > 0 and self.__personagem.vida > 0:

               
                inimigo.vida -= self.__personagem.ataque

                print(f"Personagem causou {self.__personagem.ataque} de dano")
                print(f"Vida do inimigo: {inimigo.vida}")

                if inimigo.vida <= 0:
                    print("Inimigo derrotado!")
                    break

                self.__personagem.retirar_vida(inimigo.ataque)

                print(f"Inimigo causou {inimigo.ataque} de dano")
                print(f"Vida do personagem: {self.__personagem.vida}")

            quantidade -= 1
            cont += 1

            print("----")
        if(quantidade <=0 and self.__personagem.vida > 0):
            return True
        return False
        pass
    def missao_col(self):
        print("-" * 50)
 
        quantidade_alvo = self.__missao.quantidade
        item_nome       = self.__missao.item
        velocidade      = self.__personagem.velocidade
 
        coletados  = 0
        tentativas = 0
        
        max_rounds = quantidade_alvo * 2
 
        
        chance_base = 0.60 + min(velocidade / 100, 0.30)  
 
        print(f"Objetivo: coletar {quantidade_alvo}x {item_nome}")
        print(f"Chance de encontrar por round: {chance_base * 100:.0f} %")
        print("----")
 
        while coletados < quantidade_alvo and tentativas < max_rounds and self.__personagem.vida > 0:
 
            tentativas += 1
            print(f"TENTATIVA {tentativas}")
 
            if random.random() < chance_base:
                coletados += 1
                print(f"Item encontrado! ({item_nome})  Coletados: {coletados}/{quantidade_alvo}")
            else:
                print(f"Nada encontrado nesta tentativa.  Coletados: {coletados}/{quantidade_alvo}")
 
            
            desgaste = 3
            self.__personagem.retirar_vida(desgaste)
            print(f"Desgaste: -{desgaste} de vida  |  Vida atual: {self.__personagem.vida}")
            print("----")
 
        if coletados >= quantidade_alvo and self.__personagem.vida > 0:
            print(f"Coleta concluída! {coletados} {item_nome}(s) coletados.")
            return True
 
        print(f"Coleta fracassada. Conseguiu apenas {coletados} de {quantidade_alvo}.")
        return False


#e = Engine(m,p)
#e.comecar()