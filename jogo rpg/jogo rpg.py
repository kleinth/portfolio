'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#personagens
nome = "escolha seu nome"
dano = 5
defesa = 5
vida = 100

nomeladrao = "ladrao"
danoladrao = 8
defesaladrao = 5
vidaladrao = 100
#-----------------------------------------------------
#variaveis de jogo
atkdef = None
import random
danorandom = random.randint(1,3)

ataque= None
defesanojogo= None


print(nome)

nome = input("Qual seu novo nome? ")


print("Seu novo nome é: ", nome)

print(" ")

#-----------------------------------------------------


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Distribua seus atributos")
print(" ")
print("Nome: ", nome)
print("Dano:", dano)
print("Defesa", defesa)
print("Pontos para distribuir: 3")


while True:
    answer = input('Vc quer aumentar 3 pontos em dano ou defesa? escolha (dano) ou (defesa): ')
    if answer == 'dano':
        dano = dano + 3
        print("Vc esta com ", dano, "de dano")
        break
    if answer == 'defesa':
        defesa = defesa + 3
        print("Vc esta com ", defesa, "de defesa")
        break    
    print("Por favor, digite apenas DANO ou DEFESA")


	
	
	
print(" ")
print("Vc acabou de avistar um ladrao, prepare-se para o combate")
print(" ")
	
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXxxxxxxxxxxxxxxxxx")
	

def luta():
    global vidaladrao
    global vida
    while True:
    if (vida>0) or (vidaladrao>0):
    atkdef = input("vc pode escolher entre atacar ou defender, digite a para atacar, e d para defender")
    if atkdef=="a": 
	    ataque = dano * danorandom - defesaladrao
	    print("voce causou: ", ataque, "aos pontos de vida do inimigo")
	
    vidaladrao = vidaladrao - ataque
    print("ladrao esta com ", vidaladrao, " pontos de vida")
    if vidaladrao<0:
        print("vc ganhou a luta")
        break
    if vida<0:
        print("vc morreu")
        break
    return

luta()









