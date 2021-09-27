# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 06

###################################################################
# 6) Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

contador = 1
nomeLista = []

while ( contador < 6 ):

    nomeLista.append(input(f"\nEntre com o nome do usuário de número : {contador} >> >> "))

    contador = contador + 1

print(f'\nNomes: {nomeLista}\n')

