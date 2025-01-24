valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for n in notas:
    unidades = int(valor / n)
    valor %= n
    print(f"{unidades} nota(s) de R$ {n:.2f}")

print("MOEDAS:")
for m in moedas:
    valor = round(valor, 2)
    unidades = int(valor / m)
    valor %= m
    print(f"{unidades} moeda(s) de R$ {m:.2f}")
