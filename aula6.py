import os 
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
#   case valor:


# linguagem = 100

# match linguagem: 

#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "hmtl":
#         print("kauã não dorme")
#     case 10:
#         print("entrou aqui!")
#     case _ :
#         print("outro caso")
    

# print("1- domingo","\n 2- segunda", "\n 3- terça", "\n 4- quarta", "\n 5- quinta", "\n 6- sexta", "\n 7- sexta")

# dia = int(input ("digite um numero da semana:"))
# match dia:

#     case 1:
#         print("Domingo")
#     case 2:
#         print("Segunda")
#     case 3:
#         print("Terça")
#     case 4:
#         print("Quarta")
#     case 5:
#         print("Quinta")
#     case 6:
#         print("sexta")
#     case 7:
#         print("Sábado")



# print("","VENDA DE CELULARES", sep= "*"*10, end= "*"*10)
# print(r"""
      
                                             
#             ############################          
#       ######################################@@    
#     ############################################  
#   ################                ################
#   ############                        ############
#   ############                        ############
#   ############      ############      ############
#   ##########      ################      ##########
#                   ################                
#                 ####################              
#             ##########        ##########          
#         ############            ############      
#         ############            ############      
#         ############            ############      
#         ############            ############      
#       ################        ################    
#       ########################################    
#       ########################################    
#         ####################################      
      
      
      
      
      
#       """)
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")
# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


import random


papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


opcoes = ("Pedra", "Papel", "Tesoura")
desenhos = (pedra, papel, tesoura)


print("Escolha uma opção:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")
jogador = int(input("Digite o número correspondente à sua escolha: "))


computador = random.randint(0, 2)


print(f"\nVocê escolheu:\n{desenhos[jogador]}")
print(f"O computador escolheu:\n{desenhos[computador]}")


match (jogador, computador):
    case (a, b) if a == b:
        print("Empate!")
    case (0, 2), (1, 0), (2, 1):
        print("Você venceu!")
    case _:
        print("Você perdeu!")













