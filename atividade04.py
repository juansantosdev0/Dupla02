import os
os.system("cls")

valor_produto = float(input("Informe o Valor do produto: R$ "))
forma_pagamento = int(input("Informe a Forma de Pagamento (1- A Vista, 2- A Prazo): "))

match forma_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        total = valor_produto - desconto

        print("\n--- RESUMO DO CHECKOUT ---")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: À vista")
        print(f"Desconto (10%): R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        parcelas = int(input("Informe a Quantidade de parcelas (1 a 6): "))

        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas

            print("\n--- RESUMO DO CHECKOUT ---")
            print(f"Valor do produto: R$ {valor_produto:.2f}")
            print(f"Forma de pagamento: A prazo ({parcelas}x)")
            print(f"Valor da parcela: R$ {valor_parcela:.2f}")
            print(f"Total a pagar: R$ {valor_produto:.2f}")
        else:
            print("\nNúmero de parcelas inválido! O número deve ser entre 1 e 6.")

    case _:
        print("\nForma de pagamento inválida!")