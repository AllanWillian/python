m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (10):
    m[i] = str ( input ( "Preencha o vetor com letras: " ) )

contador=0

for i in (m):
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
        contador += 1
        print(i)
print("A quantidade de consoantes é:", contador)

