#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE
#.lower() -> converte maiusculo para minusculo
#in -> dentro de um texto





#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)








# #leção
# print("*" *15, "PROGRAMA", "*" *15)
# idade= int(input("Digite sua idade: "))
# if idade >= 120 or idade <= 0:
#     print("IDADE INVALIDA!")
# else:
#     if idade >= 18:
#         print("MAIOR DE IDADE")
#     else:
#         print("MENOR DE IDADE")





# print("*" *15, "PROGRAMA2", "*" *15)
# email = "python@senai.com"
# senha = "12345"
# pergunta1 = (input("Digite seu email:"))
# pergunta2 = (input("Digite sua senha:"))

#     print("USUARIO AUTENTICADO")
# else: 
#      print("USUARIO OU SENHA INVALIDO")

#LIÇÃO
# print("*" *5, "SUPERHORTIFRUTT", "*" *5)
# qnt = int(input("digite quantas maças: "))
# if qnt < 12 :
#     calc = qnt * 0.30
#     print("Voce ira pagar: R$ " , calc)
# else: 
#     calc = qnt * 0.25
#     print("voce ira pagar: R$" , calc)


#letras
# pergunta = input("digite sua letra: ").lower()
# letra = ("a") and ("e") and ("i") and ("o") and ("u")
# if pergunta == letra:
#     print("voce digitou uma vogal")
# else:
#     print("voce digitou uma consoante")

#numero
# n1 = float(input("digite seu primeiro numero: "))
# n2 = float (input("digite o outro numero: "))
# if n1 < n2:
#     print("o numero menor é:", n1)
#     print("o numero menor é:", n2)
# else:
#     print("o numero menor é:", n2)
#     print("o numero menor é:", n1)






peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso/(altura*altura)
print(f"seu imc é: {imc :.2f}")
if imc < 17:
    print("MUITO ABAIXO DO PESO!")
elif imc > 17 and imc < 18.49:
    print("abaixo do peso!")
elif imc > 18.5 and imc < 24.99:
    print("peso normal!")
elif imc > 25 and imc < 29.99:
    print("acima do peso!")
elif imc > 30 and imc < 34.99:
    print("obesidade 1")
elif imc > 35 and imc < 39.99:
    print("obesidade 2!")
elif imc > 40:
    print(" obesidade 3! morbido")
    



















