lista= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(20):
    lista[i] = str(input("Digite o nome do candidato:"))

def ordenacao():
    lista.sort()
    print(lista)

ordenacao()