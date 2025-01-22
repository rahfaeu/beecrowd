venda1 = input().split(" ")
venda2 = input().split(" ")

cod1, quantidade1, preco1 = venda1
cod2, quantidade2, preco2 = venda2

total = (int(quantidade1) * float(preco1)) + (int(quantidade2) * float(preco2))
print(f"VALOR A PAGAR: R$ {total:.2f}")
