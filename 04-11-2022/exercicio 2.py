n = int ( input ( "Escreva um numero inteiro" ) )


def recursiva(n):
    if n == 0:
        return 1
    else:
        return n * recursiva ( n - 1 )


print ( "O resultado é:", recursiva ( n ) )
