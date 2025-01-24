a, b, c, d = map(int, input().split(" "))

b_maior_c = b > c
d_maior_a = d > a
cd_maior_ab = (c + d) > (a + b)
c_positivo = c > 0
d_positivo = d > 0
a_par = a % 2 == 0

aceito = b_maior_c and d_maior_a and cd_maior_ab and c_positivo and d_positivo and a_par

if aceito:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
