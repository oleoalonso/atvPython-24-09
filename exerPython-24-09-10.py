# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 10

###################################################################
# 10) Faça um programa que imprima a soma de todos os números pares entre dois números da sua escolha.

num1 = int(input('\nDigite o primeiro número : '))
num2 = int(input('\nDigite o segundo número : '))

lista = []
limite = num1+1

while limite <= num2-1:

    if ( limite % 2 ) == 0:
        lista.append( limite )
        limite += 2

    elif ( limite % 2 ) != 0:
        limite += 1

print(lista)
print(f'\nO resultado da soma dos números pares que estão entre {num1} e {num2} = {sum(lista)}\n')



