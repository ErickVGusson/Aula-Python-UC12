#Colete 3 valores do usuario (a, b, c) e troque os seguintes valores
# a = b
# b = c
# c = a
# imprima na tela os resultados

valorA = input( "\nDigite o 1º valor: " ) 
valorB = input( "Digite o 2º valor: " ) 
valorC = input( "Digite o 3º valor: " ) 

print( "\nValorA = " + valorA + " | ValorB = " + valorB + " | valorC = " + valorC )

temporaria = valorA
valorA = valorB
valorB = valorC
valorC = temporaria

print( "\nValorA = " + valorA + " | ValorB = " + valorB + " | valorC = " + valorC )