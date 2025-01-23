intervalo_segundos = int(input())

horas = intervalo_segundos // 3600
minutos = (intervalo_segundos % 3600) // 60
segundos = (intervalo_segundos % 3600) % 60

print(f"{horas}:{minutos}:{segundos}")
