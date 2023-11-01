# colete 3 numeros do usuario, e ordene em ordem crescente


valor1 = float( input("Digite o 1º Valor: ") )
valor2 = float( input("Digite o 2º Valor: ") )
valor3 = float( input("Digite o 3º Valor: ") )


# Achando o menor valor
if ( valor1 < valor2 and valor1 < valor3 ):
    temp1 = valor1
elif ( valor2 < valor1 and valor2 < valor3 ):
    temp1 = valor2
elif ( valor3 < valor1 and valor3 < valor2 ):
    temp1 = valor3

# Achando o valor do meio
if ( ( valor1 < valor2 and valor1 > valor3 ) or ( valor1 > valor2 and valor1 < valor3 ) ):
    temp2 = valor1
elif ( ( valor2 < valor1 and valor2 > valor3 ) or ( valor2 > valor1 and valor2 < valor3 ) ):
    temp2 = valor2
elif( ( valor3 < valor1 and valor3 > valor2 ) or ( valor3 > valor1 and valor3 < valor2 ) ):
    temp2 = valor3

# Achando o maior valor
if ( valor1 > valor2 and valor1 > valor3 ):
    temp3 = valor1
elif ( valor2 > valor1 and valor2 > valor3 ):
    temp3 = valor2
elif ( valor3 > valor1 and valor3 > valor2 ):
    temp3 = valor3


print(' | Valor 1: ' , temp1)
print(' | Valor 2: ' , temp2)
print(' | Valor 3: ' , temp3)