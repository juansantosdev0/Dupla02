import os
os.system('cls')

total_pagar = 0.0
qtd_pratos = 0

print("--- CARDÁPIO SABOR DA TERRA ---")
print("1 - Prato Feito (PF) - R$ 20.00")
print("2 - Lasanha - R$ 25.00")
print("3 - Salada Completa - R$ 15.00")
print("4 - Hambúrguer Artesanal - R$ 22.00")
print("5 - Sumo Natural - R$ 8.00")
print("--------------------------------")

while True:
    codigo = input("Digite o código do prato desejado: ")

    match codigo:
        case "1":
            preco = 20.00
            prato = "Prato Feito (PF)"
        case "2":
            preco = 25.00
            prato = "Lasanha"
        case "3":
            preco = 15.00
            prato = "Salada Completa"
        case "4":
            preco = 22.00
            prato = "Hambúrguer Artesanal"
        case "5":
            preco = 8.00
            prato = "Sumo Natural"
        case _:
            print("Código inválido! Tente novamente.")
            continue

    total_pagar += preco
    qtd_pratos += 1
    print(f"{prato} adicionado ao pedido! (R$ {preco:.2f})")

    deseja_outro = input("\nDeseja outro prato? (S/N): ").strip().upper()
    if deseja_outro == 'N':
        break

print("\n--- RESUMO DO PEDIDO ---")
print(f"Quantidade de pratos: {qtd_pratos}")
print(f"Total a pagar: R$ {total_pagar:.2f}")