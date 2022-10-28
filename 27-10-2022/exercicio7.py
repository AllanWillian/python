#HORARIO
turno= str(input("Em que turno voce estuda? m - Matutino, v - Vespertino, n - Noturno: "))
match turno:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa noite!")


