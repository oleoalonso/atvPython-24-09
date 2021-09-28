# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 09

###################################################################
# 9) Faça um programa que imprima a quantidade de números pares entre dois números da sua escolha.

num1 = int(input("\nEntre com o primeiro número : "))
num2 = int(input("\nEntre com o segundo número : "))

limite = 0

for x in range ( num1+1, num2-1 ):
    if ( x % 2 == 0 ):
        limite += 1
    else: 
        continue

print(f'\nEntre os números {num1} e {num2} existem {limite} números pares.\n')

