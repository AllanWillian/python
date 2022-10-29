n1= float(input("Digite a nota do primeiro bimestre:"))
n2= float(input("Digite a nota do segundo bimestre:"))
n3= float(input("Digite a nota do terceiro bimestre:"))
n4= float(input("Digite a nota do quarto bimestre:"))

nota = (n1 + n2 + n3 + n4)
if nota <= 59:
    print("Você foi reprovado!")
elif nota >= 60:
    print("Você foi aprovado!")
elif nota >=40 and 60:
    print("Você esta de recuperação!")
else:
    print("Valor invalid")

