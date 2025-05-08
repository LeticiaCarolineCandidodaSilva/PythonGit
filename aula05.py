#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA,  SE ESTIVER CERTA, SAI DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")



# print("*" *15, "BOLETIM", "*" *15)
# nota1 = float(input("digite sua nota: "))
# nota2 = float(input("digite sua nota: "))
# media = (nota1+nota2)/2
# if media < 5:
#     print("reprovado")
# elif media > 5 and media < 7:
#     print("em recuperação")
# elif media > 7:
#     print("aprovado")
# print("sua media é: ", media)

# #atividade 1
# #replace("valor1", "valor2") -› Substitui o valor 1 pelo valor2 
# n1 = float(input("digite a 1º nota: ").replace(",","."))
# n2 = float(input("digite a 1º nota: ").replace(",","."))
# media = (n1+n2)/2
# #:.2f -> formata para 2 casas decimais apenas no fstring
# print(f"Média: {media: 2f}")
# if media <5:
#     print ("REPROVADO" )
# elif media >=5 and media<=7:
#     print("EM RECUPERAÇÃO")
# else:
#     print("APROVADO")


#atividade
# peso = float(input("digite seu peso: "))
# altura = float(input("digite sua altura: "))
# imc = peso/(altura*altura)
# print(f"seu imc é: {imc :.2f}")
# if imc < 17:
#     print("MUITO ABAIXO DO PESO!")
# elif imc > 17 and imc < 18.49:
#     print("abaixo do peso!")
# elif imc > 18.5 and imc < 24.99:
#     print("peso normal!")
# elif imc > 25 and imc < 29.99:
#     print("acima do peso!")
# elif imc > 30 and imc < 34.99:
#     print("obesidade 1")
# elif imc > 35 and imc < 39.99:
#     print("obesidade 2!")
# elif imc > 40:
#     print(" obesidade 3! morbido")

print("", "AUTOCAR", sep= "*" *100, end= "*" *100)
print(r"""
                       ____________________                              
                     //|           |        \                            
                   //  |           |          \                          
      ___________//____|___________|__________()\__________________      
    /__________________|_=_________|_=___________|_________________{}    
    [           ______ |           | .           | ==  ______      { }   
  __[__        /##  ##\|           |             |    /##  ##\    _{# }_ 
 {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
             /  ##__##                              /  ##__##        \   
""")

print("*" *100)
salarioatual= float(input("Digite seu salario: "))
print("a. Salários até R$ 2799.99 :aumento de 20%", "\n b.Salários entre R$ 2800,00 e R$6999,99: aumento de 15%" , "\n c.Salários entre R$ 7000,00 e R$ 14999,99: aumento de 10%")
print("d.Salários de R$ 15000,00 em diante: aumento de 5%")
valoraumento1 = 0.20 * salarioatual
valoraumento2 = 0.15 * salarioatual
valoraumento3= 0.10 * salarioatual
valoraumento4= 0.05 * salarioatual
if salarioatual <= 2799.99:
    print("\n Salario atual: " , "Percentual da sua faixa: 20%" , "\n Aumento de salario: ", valoraumento1 , "\n Novo salario: " , valoraumento1+salarioatual )
elif salarioatual >= 2800.00 and salarioatual <= 6999.99 :
    print("\n Salario atual: " , "Percentual da sua faixa: 15%" , "\n Aumento de salario: ", valoraumento2 , "\n Novo salario: " , valoraumento2+salarioatual )
elif salarioatual >= 7000.00 and salarioatual <= 14999.99 :
    print("\n Salario atual: " , "Percentual da sua faixa: 10%" , "\n Aumento de salario: ", valoraumento3 , "\n Novo salario: " , valoraumento3+salarioatual )
else:
    print("\n Salario atual: " , "Percentual da sua faixa: 5%" , "\n Aumento de salario: ", valoraumento4 , "\n Novo salario: " , valoraumento4+salarioatual )