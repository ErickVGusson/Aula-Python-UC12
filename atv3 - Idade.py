#Verificar a idade do usuario

idade = int( input( 'Digite a sua idade: ' ) )

if ( idade < 8 ):
    print( 'Voçê é um bebe' )
elif ( idade >= 8 and idade <= 13 ):
    print( 'Você é uma criança' )
elif ( idade >= 14 and idade <= 20 ):
    print( 'Você é um adolescente' )
elif ( idade >= 21 and idade <= 64 ):
    print( 'Você é um adulto' )
else :
    print( 'Você é um idoso' )