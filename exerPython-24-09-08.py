# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 08

###################################################################
# 8) Faça um programa, utilizando while e listas, 
# que permita o usuário realizar o cadastro de um número indeterminado de pessoas enquanto quiser 
# e os mostre na tela ao finalizar.

continuar = "Sim"
pessoasLista = []

while ( continuar == "S" or continuar == "s" or continuar == "Sim" or continuar == "SIM" or continuar == "sim" ):

    pessoasLista.append(input(f"\nEntre com o nome : "))

    continuar = input("\nContinuar ?\n\n Digite (S)im ou (N)ão : ")

print(f'\nNomes: {pessoasLista}\n')