n1, n2, n3, n4 = map(float, input().split(" "))

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print(f"Media: {media:.1f}")
if media < 5:
    print("Aluno reprovado.")
    quit()

if media >= 7:
    print("Aluno aprovado.")
    quit()

if media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final > 5:
        print("Aluno aprovado.")
    else:
        print("Aluno aprovado.")
    print(f"Media final: {media_final:.1f}")








