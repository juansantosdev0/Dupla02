import os
os.system("cls")

nome_produto = input("Informe o nome do produto:")
quantidade = int(input("Informe a quantidade do produto: "))
preco_uninatario = float(input("Informe o valor do produto:"))

total = quantidade * preco_uninatario

if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05


desconto = total * percentual_desconto
total_a_pagar = total - desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"produtos: {nome_produto}")
print(f" total bruto: R$ {total:.2f}")
print(f"Desconto ({int(percentual_desconto * 100)}%): R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
