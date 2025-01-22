a, b, c = map(float, input().split(" "))

pi = 3.14159

# a) a área do triângulo retângulo que tem A por base e C por altura: área = (base * altura) / 2
triangulo = (a * c) / 2

# b) a área do círculo de raio C. (pi = 3.14159): área = pi * r ** 2
circulo = pi * c ** 2

# c) a área do trapézio que tem A e B por bases e C por altura. área = ((base + base) * altura) / 2
trapezio = (a + b) * c / 2

# d) a área do quadrado que tem lado B: lado ** 2
quadrado = b ** 2

# e) a área do retângulo que tem lados A e B: área = altura * largura
retangulo = a * b

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
