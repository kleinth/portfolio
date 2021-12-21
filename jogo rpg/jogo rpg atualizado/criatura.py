import random


class Criatura:

    def __init__(self, nome, vida, dano, defesa, pontos_livres):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.defesa = defesa
        self.pontos_livres = pontos_livres

    def atacar(self, alvo, bonus_defesa):
        multiplicador = random.randint(1, 3)
        dano = max(self.dano * multiplicador - (alvo.defesa + bonus_defesa), 0)
        alvo.vida = alvo.vida - dano
        print(self.nome, " causou ", dano, " de dano em ", alvo.nome)

    def exibir_vida(self):
        print("vc esta com ", max(self.vida, 0), " de vida")

    def descrever(self):
        print("Nome: ", self.nome)
        print("Dano:", self.dano)
        print("Defesa", self.defesa)
        print("Pontos para distribuir: ", self.pontos_livres)
