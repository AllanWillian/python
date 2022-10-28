#CALCULADORA
repetir:str = ("s" or "n")
while repetir == "s":
    n1= int(input("Digite o primeiro numero:"))
    sn= str(input("Qual sinal voce precisará? + , -, *, /"))
    n2= int(input("Digite o segundo numero:"))
    if sn == "+":
        print("A soma de:", n1 ,"+", n2,"é", n1+ n2)
    elif sn == "-":
        print ( "A subtração de:", n1, "-", n2, "é", n1 - n2 )
    elif sn== "*":
        print ( "A multiplicação de:", n1, "*", n2, "é", n1 * n2 )
    elif sn == "/":
        print ( "A divisao de:", n1, "/", n2, "é", n1 / n2 )
    resposta = input("Deseja continuar?,s/n?")




