codigo, quantidade = map(int, input().split(" "))

codigo -= 1

tabela = [
    {"codigo": 1, "espec": "Cachorro Quente", "preco": 4.00},
    {"codigo": 2, "espec": "X-Salada",        "preco": 4.50},
    {"codigo": 3, "espec": "X-Bacon",         "preco": 5.00},
    {"codigo": 4, "espec": "Torrada simples", "preco": 2.00},
    {"codigo": 5, "espec": "Refrigerante",    "preco": 1.50},
]

total = quantidade * tabela[codigo]["preco"]
print(f"Total: R$ {total:.2f}")
