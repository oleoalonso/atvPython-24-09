# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 02

###################################################################
# 2) Faça um Programa que leia três números inteiros e mostre o maior deles.

num1 = int(input("\nEntre com o primeiro número inteiro : "))
num2 = int(input("\nEntre com o segundo número inteiro : "))
num3 = int(input("\nEntre com o terceiro número inteiro : "))

if num1 > num2 and num1 > num3 :
    print(f"\n{num1} É o maior número\n")

elif num2 > num1 and num2 > num3 :
    print(f"\n{num2} É o maior número\n")

elif num3 > num1 and num3 > num2 :
    print(f"\n{num3} É o maior número\n")