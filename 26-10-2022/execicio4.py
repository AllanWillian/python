#LOJA DE CELULARES (EXERCICIO)
iphone = 2980
samsung = 2540
tablet= 1950
ps5=2100
notebook= 2350

#QUANTIDADE EXIGIDA PELO CLIENTE
quantiphone = int (input ("quantos iphone voce deseja?" ))
quantsamsung = int (input ("quantos samsung voce deseja?"))
quantablet = int (input ("quantos tablet voce deseja?" ))
quantps5 = int (input ("quantos ps5 voce deseja?"))
quantnot = int (input ("quantos notebook voce deseja?"))

#TOTAL DA COMPRA
total= (iphone*quantiphone) + (samsung * quantsamsung)+ (tablet* quantablet)+ (ps5 * quantps5) + (notebook *quantnot)
print("O total da compra é: R$", total)

#PARCELAMENTO DE 3X
parcela3 = round(total/3, 2)
print("O valor da parcela é: R$", parcela3)

#PARCELA DE 6X COM 5% DE JUROS
parcela6 = (total*1.05) /6
print("O valor da parcela com o juros é: R$", parcela6)

#DESCONTO DE 10%
desconto10 = total - (total * 0.10)
print("O valor com desconto é:R$",desconto10)

print("Muito obrigado pela preferencia!!!!")



