import os 
os.system("cls")
#Estrutura de repetição for
# o numero colocado no range é a quantidade a ser repetido
# por doas praticas usa-se a variavel i no for, porem pode ser qualquer nome


# for com 1 paraetro 
# for i in range(10): #i começa em0 e termina em 9 
#     print("senai", i)

# #for com 2 parametros
# for i in range(20,30): #i começa em 20 e vai ate range 29 (20 a 29)
#     print(i)

#for com 3 parametros
# for i in range (0,10,5): #i começa em 0 e vai ate 5
#     print(i)

#Atividade 1 
# for i in range(1,50):
#     print(i)

# #Atividade 2
# for i in range(-30, 16):
#     print(i)

#Atividade 3
# tabuada = int(input("Digite um número: "))

    
# for i in range(1, 11):
#     print(f"{i} x {tabuada} = {i*tabuada}")

#Atiidade 4
# n=0
# maior=0
# for i in range(5):
#     n= int(input("Digite um numero: "))
#     if n > maior:
#         maior = n

# print("O maior número digitado foi:", maior)


#Atividade 5
# paes = float(input("Digite o preço da unidade do pão: "))
# for i in range(1,51):
#     print(f"{i}= R${i*paes:.2f} ")

# qpaes= int(input("Digite a quantidade de pães:"))
# valor= round((paes*qpaes), 2)
# print("Total da compra: ", valor)
# formadepag= (input("Forma de pagamento: NOTA2|NOTA5|NOTA10|NOTA20|NOTA50: ")).upper()
# match formadepag:
#     case "NOTA2":
#         nota2 = 2
#     case "NOTA5":
#         nota5= 5
#     case "NOTA10":
#         nota10= 10
#     case "NOTA20":
#         nota20 = 20
#     case "NOTA50":
#         nota50= 50
# desconto= input("Digite o cupom de desconto: " )

# if desconto == "paodeontem":
#     descontovalor = round(valor * 0.10, 2)
#     valorcomdesconto = round(valor - descontovalor,2)
#     print("Aplicado 10% de desconto ---> TOTAL: R$ ", valorcomdesconto)
# else:
#     print("Cupom inválido! Sem desconto aplicado. TOTAL: R$", valor)
# if formadepag > valorcomdesconto:
#     troco = round(formadepag - valorcomdesconto, 2)
#     print(" Troco: R$ ", troco)
# else:
#     faltando= round(valorcomdesconto - formadepag, 2)
#     print("Pagamento insuficiente. Faltam R$ ", faltando)

# precoPao= float(input("Digite o preço do pao: "))  

# print("PANIFICADORA PAO MURCHO")

# for i in range(1,51):
#     print(i,f" - R$:{round(precoPao*i,2)}")

# qtd = int(input("Digite a quantidade que gostaria de levar: "))
# total =  round(precoPao * qtd,2)
# print("TOTAL SEM DESCONTO: ",total)
# cupom = input("digite o cupom de desconto: ")

# if cupom =="paodeontem":
#     total = round(total - (total *0.10),2)
# else:
#     print("CUPOM INVÁLIDO!")


# print(f"TOTAL DA COMPRA: {total}")

# pagto = int(input("Digite a forma de pagto (APENAS O VALOR): NOTA2 | NOTA 5 | NOTA 10 | NOTA 50"))

# if pagto > total: 
#     print("TROCO DE R$: ", round(pagto - total,2))
# elif pagto < total: 
#     print(" DINHEIRO INSUFICIENTE , FALTAM R$: ", round(total-pagto,2))
# else:
#     print("NÃO TEM TROCO , PAGAMENTO OK!")


# print("", "INSCRIÇÕES", sep="*"*10,end="*"*10)
# voto1= 0
# voto2=0
# voto3=0
# candidato1= input("\nDigite o nome do primeiro candidato: ")
# nc1= int(input("Digite o número do candidato: "))
# candidato2= input("Digite o nome do segundo candidato: ")
# nc2= int(input("Digite o número do candidato: "))
# candidato3= input("Digite o nome do terceiro candidato: ")
# nc3= int(input("Digite o número do candidato: "))
# print("", "VOTAÇÃO", sep="*"*10, end="*"*10)
# print("\nParticipantes: ", "\nPara votar em ", candidato1, "Digite ", nc1, "\nPara votar em ", candidato2, "Digite ", nc2, "\nPara votar em ", candidato3, "Digite ", nc3)
# for i in range (1,11):

#     votacao= int(input("digite o numero do candidato para votar: "))
#     if votacao ==nc1:
#        voto1= voto1+1
#        print("CANDIDATO VOTADO",candidato1)
#     elif votacao == nc2:
#        voto2= voto2+1
#        print("CANDIDATO VOTADO",candidato2)
#     elif votacao==nc3:
#         voto3= voto3 + 1
#         print("CANDIDATO VOTADO",candidato3)
        
#     else:
#         print("CANDIDATO NÃO ENCONTRADO, VOTO NULADO!")
# print("", "RESULTADO DA VOTAÇÃO", sep="*"*10,end="*"*10)
# max= max(voto1, voto2, voto3)
# if voto1 == voto2:
#     print("EMPATE!, Outro turno será concluido.")
# elif voto2 == voto3:
#     print("EMPATE!, Outro turno será concluido.")
# elif voto3 == voto1:
#     print("EMPATE!, Outro turno será concluido.")
# elif voto1 > voto2 and voto1 > voto3:
#     print(voto1, "GANHOU!, votação encerrada.")
# elif voto2 > voto3 and voto2 > voto1:
#     print(voto2, "GANHOU!, votação encerrada.")
# elif voto3 > voto1 and voto3 > voto2:
#     print(voto3, "GANHOU!, votação encerrada.")




#resoluçao

# candidato1 = input("Digite seu nome: ")
# candidato1Numero = input("Digite seu numero de candidatura: ")
# candidato1Voto=0

# candidato2 = input("Digite seu nome: ")
# candidato2Numero = input("Digite seu numero de candidatura: ")
# candidato2Voto=0

# candidato3 = input("Digite seu nome: ")
# candidato3Numero = input("Digite seu numero de candidatura: ")
# candidato3Voto=0

# print("-"*60)

# print(f"""
# 	ELEIÇÃO CANDIDATOS:
# 	{candidato1} pressionar {candidato1Numero}
# 	{candidato2} pressionar {candidato2Numero}
# 	{candidato3} pressionar {candidato3Numero}
#   """) 

# for i in range(10):
# 	voto = input("Digite o numero do candidato para votar: ")
    
# 	if voto == candidato1Numero or voto == candidato2Numero or voto ==candidato3Numero:
# 		match voto: 
# 			case _ if voto == candidato1Numero:
# 				candidato1Voto =  candidato1Voto +1 
# 				print(f"VOTO COMPUTADO PARA {candidato1}")

# 			case _ if voto == candidato2Numero:
# 				candidato2Voto =  candidato2Voto +1 
# 				print(f"VOTO COMPUTADO PARA {candidato2}")

# 			case _ if voto == candidato3Numero:
# 				candidato3Voto =  candidato3Voto +1 
# 				print(f"VOTO COMPUTADO PARA {candidato3}")

# 	else:
# 		print("CANDIDATO NÃO ENCONTADO, VOTO ANULADO!")

# print("RESULTADO DA ELEIÇÃO: ")
# print(f""" 

# 	{candidato1} : {candidato1Voto} votos
# 	{candidato2} : {candidato2Voto} votos
# 	{candidato3} : {candidato3Voto} votos

# """)

# maiorVoto = max(candidato1Voto,candidato2Voto,candidato3Voto)

# if maiorVoto == candidato1Voto and candidato1Voto != candidato2Voto and candidato1Voto != candidato3Voto:
# 	print(f"VENCEDOR {candidato1}")
# elif maiorVoto == candidato2Voto and candidato2Voto != candidato1Voto and candidato2Voto != candidato3Voto:
# 	print(f"VENCEDOR {candidato2}")
# elif maiorVoto == candidato3Voto and candidato3Voto != candidato1Voto and candidato3Voto != candidato2Voto:
# 	print(f"VENCEDOR {candidato3}")
# else:
# 	print(" VOTAÇÃO EMPATADA , SERA NECESSARIO NOVO TURNO!")













    



    