a = float(input())
b = float(input())
c = float(input())

peso_a = 2
peso_b = 3
peso_c = 5

a *= peso_a
b *= peso_b
c *= peso_c

media = (a + b + c) / (peso_a + peso_b + peso_c)
print(f'MEDIA = {media:.1f}')
