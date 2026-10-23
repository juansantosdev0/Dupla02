import os
os.system('cls')

notas = []

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
    
    while nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.")
        nota = float(input(f"Digite a {i}ª nota novamente: "))
        
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")