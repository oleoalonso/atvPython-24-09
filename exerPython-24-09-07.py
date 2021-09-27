# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 07

###################################################################
# 7) Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.


continuar = input("\nDeseja efetuar uma adição ? \n\nDigite (S)im ou (N)ão : ")

while ( continuar == "S" or continuar == "s" or continuar == "Sim" or continuar == "SIM" or continuar == "sim" ):

    num1 = int(input("\nEntre com o primeiro número : "))
    num2 = int(input("\nEntre com o segundo número : "))

    resultado = ( num1 + num2 )

    print(f"\n{num1} + {num2} = {resultado}")

    continuar = input("\nContinuar ?\n\n Digite (S)im ou (N)ão : ")

print("\n\nAté mais ...\n\n")


