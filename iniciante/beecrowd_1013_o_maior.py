a, b, c = map(float, input().split(" "))

def maior_numero(x, y):
    return (x + y + abs(x - y)) / 2

maior_ab = int(maior_numero(a, b))
maior_abc = int(maior_numero(maior_ab, c))

print(f"{maior_abc} eh o maior")
