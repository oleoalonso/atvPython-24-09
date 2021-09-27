# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python [24/09] 05

###################################################################
# 5) Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.

limite = int(input("\nEntre com o valor limite : "))
x = 0
while x < limite + 1:
  print(x)
  x += 1