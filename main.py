soma = 0

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: ")) 
    soma += nota

media = soma / 5

print(f"A média das notas é: {media:.2f}")

if media >= 6:
    print("Classificação: Aprovado")
else:
    print("Classificação: Reprovado")