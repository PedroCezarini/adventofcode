arq = open("smc.txt")
calibration_value = 0

for linha in arq:
    linha_lst = []

    for carac in linha:

        if carac.isdigit():
            linha_lst.append(carac)
            
    print(linha_lst)
    print(linha_lst[0])
    print (linha_lst[-1])
    calibration = linha_lst[0] + linha_lst[-1] #concatenando os 2 index em uma string
    print(int(calibration)) #aqui que tá sendo feito o casting momentaneo dessa string para int

    #o problema tava na ordem de concatenar e transformar em int, foi só ajustar essa ordem




    calibration_value = calibration_value+int(calibration)#aqui tá sendo feito o casting momentaneo dessa string para int para usar na soma

    print(type(calibration))

print(calibration_value)  



#for i=0 , ate o fim da linha
    #para armazenar, precisa ter 2 digitos, e preciso armazenar o primeiro e o ultimo
    #agora eu preciso tratar os casos que não atendem o criterio basico, ou seja, que tem 
    


arq.close()
