#12 red cubes , 13 green cubes , 14 blue cubes
#which games are possible with these options?
#a manha nesse eh dividir com o split

#agora converter o numero q sai em numeroCor[1] em int, e somar tipo azul = azul + numeroCor[1]
arq = open("gameInput.txt")
i = int(1)
j = int(1)

for linha in arq:                                                               # Cria uma lista em q cada linha do arq eh um indice
    linhaSeparada = linha.split(':')
    
    azul = int(0)
    verde = int(0)
    vermemlho = int(0)
    
    jogos = linhaSeparada[1].split(';')                                         # Jogos eh uma lista, onde cada rodada separada por ; eh um elemento dela.
    print("Jogo ",i)
    i=i+1
    
    for rodada in jogos:
        jogadas = rodada.split(',')                                             # Jogadas eh uma lista onde cada indice eh um numero e cor
        print()        
        
        for turno in jogadas:
            numeroCor = turno.split(' ')
            print(numeroCor)
            
            if numeroCor[2] == 'red':
                print("Tem vermelho")
            if numeroCor[2] == 'green':
                print("Tem verde")
            if numeroCor[2] =='blue':
                print("Tem azul")
         
        
        
    print('---------------------------')
    
    

















'''
for linha in arq:
    eliminaInutil = linha.split(':')

    jogos = eliminaInutil[1].split(';')     # a partir daqui ja tenho uma lista com as rodadas de cada jogo
    #print (jogos)                           # a variavel jogos está armazenando todas as rodadas de cada game
    print("------------")
   
    
    for jogo in jogos:
        rodadas = jogo.split(',')

        azul = 0
        vermelho = 0
        verde = 0
        

        for cor in rodadas: #aqui ta separado por cores
            a = cor.split() #aqui a gente separa o valor e a cor como elementos diferentes [0] e [1] da lista a

            if a[1] == 'blue':
                azul = azul + int(a[0])
                if azul > 14:
                    print("não é possível elfo")
                else:
                    print("O AZUL EH POSSIVEL SIM SR ELFO")
                print("*******************")
            
            if a[1] == 'red':
                vermelho = vermelho + int(a[0])
                if vermelho > 12:
                    print("não é possível elfo")
                else:
                    print("EH POSSIVEL SIM SR ELFO")

            if a[1] == 'green':
                verde = verde + int(a[0])
                if verde > 13:
                    print("não é possível elfo")
                else:
                    print("EH POSSIVEL SIM SR ELFO")

            
            print(a[0], a[1])
            print("blue", azul, "red", vermelho, "green", verde)
    
        
        print()
'''