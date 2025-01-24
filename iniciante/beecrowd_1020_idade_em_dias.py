idade_em_dias = int(input())

ano = idade_em_dias // 365
mes = idade_em_dias % 365 // 30
dia = idade_em_dias % 365 % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
