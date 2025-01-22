vendedor = str(input())
salario_fixo = float(input())
venda_total = float(input())

comissao = venda_total * 0.15
total = salario_fixo + comissao

print(f"TOTAL = R$ {total:.2f}")