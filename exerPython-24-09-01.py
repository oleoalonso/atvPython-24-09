# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 01

###################################################################
# 1) Faça um programa que pergunta a idade do usuário e informe se ele está apto a votar ou não.
# Voto obrigatório!	De 18 até 70
# Voto opcional!	Entre 16 e menores de 18
# Voto inválido!	Menos de 16

idade = int(input("\nEntre com a idade : "))

if idade >= 18 and idade <= 70 :
    print("\nVoto obrigatório!\n")

elif idade >= 16 and idade <= 18 :
    print("\nVoto opcional!\n")

elif idade < 16 :
    print("\nVoto inválido!\n")