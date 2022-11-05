#Faça um Programa que leia dois vetores com 10 posições cada e receba números inteiros.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Mostre ao final os três vetores.


v1= []
for i in range (10):
    vetor1. append(int(input("Preencha o primeiro vetor com 10 numeros: ")))


v2=[]
for i in range (10):
    vetor2.append(int(input("Preencha o segundo vetor com 10 numeros: ")))

res= v1 +v2
res[::2] = v1
res[1::2] = v2
print("vetor 3 é:", res)