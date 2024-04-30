#12 red cubes , 13 green cubes , 14 blue cubes
#which games are possible with these options?
#a manha nesse eh dividir com o split
arq = open("gameInput.txt")

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


       
        


''''
for linha in arq:
    jogos = linha.split(':')

    a = jogos[1].split(';')

    for rodada in a:
        b = rodada.split(',')

        for c in b:
            print(c)

        for i, tentativa in enumerate(rodada):
            print(rodada, tentativa)

    for i, jogo in enumerate(separaJogos):
        tentativa = jogo.split(',')
        print(i, jogo)
        print ()
        
        for cor in tentativa:
            cor = cor.split()
            print(cor)

            if 'blue' in cor:
                print('tem azul')
            
            if 'red' in cor:
                print('tem vermelho')

            if 'red' in cor:
                print('tem vermelho')

'''
