import os 
os.system ("cls")

#ATIVIDADE 1
# senha= 1505
# while senha == 1505: 
#     tentativa= int(input("Digite sua senha: "))
#     if tentativa == senha:
#         print("Senha Correta!")
#     elif tentativa == 9999:
#         print("programa fechado")
#     elif tentativa != senha or tentativa != 9999:
#         print("Senha incorreta!")
#     elif tentativa == 9999:
#         print("programa fechado")

# #ATIVIDADE2
# import random
# usuario=0
# maquina= 1
# while usuario != maquina:
#     maquina= random.randint(1,10)
#     pergunta= int(input("Digite seu numero: "))
#     print("Voce escolheu: ", pergunta, "\nComputador escolheu: ", maquina)
#     if pergunta != maquina:
#         print("\n Incorreto")
# if pergunta == maquina:
#     print("\nACERTOU!")



# #ATIVIDADE 3
# print("", "CAIXA ELETRONICO", sep="*"*10,end="*"*10)
# print("""
# 1- Deposito
# 2- Saque
# 3- Saldo
# 4- Sai do programa
#       """)
# saldo= 0
# opcao=0
# while saldo != 4:
#     opcao= int(input("Digite a sua opção: "))
#     if opcao == 1:
#             deposito= float(input("Qual valor gostaria de depositar?: " ))
#             saldo= saldo + deposito
#     elif opcao == 2:
#             saque= float(input("Qual valor gostaria de sacar?: " ))
#             saldo= saldo - saque
#     elif opcao == 3:
#                  print("SALDO: ", saldo)
#     elif opcao == 4:
#             print("Saiu do caixa")
#             break


#Atividade 4
opcao=0
pergunta1= int(input("Digite o primeiro número: "))
pergunta2= int(input("Digite o segundo número: "))
while opcao != 5:
    print("", "MENU", sep="*"*10,end="*"*10)
    print("""
    1- Somar
    2- Multiplicar
    3- Maior   
    4- Novos números
    5- Sair do programa    
          """)
    opcao= int(input("Digite a opção: "))
    if opcao == 1:
        print("A soma entre: ", pergunta1, "+", pergunta2, ":", pergunta1 + pergunta2)
    elif opcao == 2:
         print("A multiplicação entre: ", pergunta1, "x", pergunta2, ":", pergunta1 + pergunta2)
    elif opcao == 3:
        maiornumero= max(pergunta1,pergunta2)
        print(maiornumero)
    elif opcao == 4:
        pergunta1= int(input("Digite o primeiro novo número: "))
        pergunta2= int(input("Digite o segundo novo número: "))
    elif opcao == 5:
        print("Sai do programa")
        break




