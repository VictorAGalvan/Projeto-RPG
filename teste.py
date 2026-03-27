from missao import Missao
from personagem import Personagem
try:
    p1 = Personagem("Victor")
    m1 = Missao("Matar dragão", "matar o Dragão de Fogo em tal lugar", 10)
    m1.status= "Concluida"
except Exception as e:
    print(e)
else:
    print(m1.descricao)
    print(m1)
