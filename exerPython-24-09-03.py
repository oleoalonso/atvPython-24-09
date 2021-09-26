# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 03

###################################################################
# 3) Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

num1 = int(input("\nEntre com o primeiro número inteiro : "))
num2 = int(input("\nEntre com o segundo número inteiro : "))
num3 = int(input("\nEntre com o terceiro número inteiro : "))
numMaior = 0
numMenor = 0


if num1 > num2 and num1 > num3 :
    numMaior = num1

elif num2 > num1 and num2 > num3 :
    numMaior = num2

elif num3 > num1 and num3 > num2 :
    numMaior = num3

elif num1 < num2 and num1 < num3 :
    numMenor = num1

elif num2 < num1 and num2 < num3 :
    numMenor = num2

elif num3 < num1 and num3 < num2 :
    numMenor = num3    

print(f"\n{numMaior} É o maior número\n") 
print(f"{numMenor} É o menor número\n")     