from criatura import Criatura

jogador = Criatura("Jogador", 100, 5, 5, 3)
ladrao = Criatura("Ladrão", 100, 8, 5, 0)


def trocar_nome(criatura):
    criatura.nome = input("Qual seu novo nome? ")

    print("Seu novo nome é: ", jogador.nome)
    print(" ")


def distribuir_pontos(criatura):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Distribua seus atributos")
    print(" ")
    criatura.descrever()

    while True:
        answer = input(
            "Vc quer aumentar em " + str(criatura.pontos_livres) + " pontos em dano ou defesa? escolha (dano) ou (defesa): ")

        if answer == 'dano':
            criatura.dano = criatura.dano + 3
            print("Vc esta com ", criatura.dano, "de dano")
            break
        elif answer == 'defesa':
            criatura.defesa = criatura.defesa + 3
            print("Vc esta com ", criatura.dano, "de defesa")
            break
        else:
            print("Por favor, digite apenas DANO ou DEFESA")


def luta():
    atkdef = input("you can choose to either attack or defend, A or D")
    if atkdef == "a":
        jogador.atacar(ladrao, 0)
        ladrao.atacar(jogador, 0)

    if atkdef == "d":
        ladrao.atacar(jogador, 3)

    jogador.exibir_vida()


def jogo_terminou():
    if ladrao.vida < 1:
        print("vc matou o inimigo, vc venceu")
        return True
    if jogador.vida < 1:
        print("vc morreu!")
        return True
    return False


def jogo():
    trocar_nome(jogador)
    distribuir_pontos(jogador)

    print(" ")
    print("Vc acabou de avistar um ladrao, prepare-se para o combate")
    print(" ")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    while not jogo_terminou():
        luta()


jogo()
