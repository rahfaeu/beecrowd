valor = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for n in cedulas:
    unidades = valor // n
    valor %= n
    print(f"{unidades} nota(s) de R$ {n},00")
