'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
vida = 100
vidaladrao = 100
dano = 5
defesa = 5
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


while True:
    global vidaladrao
    global vida
    vida > 0
    uppoint = input("Vc quer atacar ou defender? (A) OU (D)")
    if uppoint == 'a':
        ataque = dano * danorandom - defesaladrao
        print("Voce causou: ", ataque, "aos pontos de vida do inimigo")





        #if atkdef=="a": 
	    #ataque = dano * danorandom - defesaladrao
	    #print("voce causou: ", ataque, "aos pontos de vida do inimigo")


        while True:
            global vida
            global vidaladrao
            if vida>0:
                
                if vida<=0:
                    break