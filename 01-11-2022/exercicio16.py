hora = float ( input ( "Quantos voce ganha por horas trabalhadas?" ) )
ht = float ( input ( "Qual é o numero de horas que voce trabalha por mes?" ) )
result = hora * ht
print ( "O salario bruto é R$", result, "mes" )

ir = result * 0.11
print("O valor descontado do imposto de renda é:", ir)
inss = result * 0.08
print("O valor descontado do INSS é:", inss)
sd = result * 0.05
print("O valor descontado do sindicato é:", sd)


total = result- (ir+inss+sd)
print("O meu salario é: R$ ", total)