import os 
os.system("cls")

total_familias = 0
soma_salario = 0.0
soma_filhos = 0
maior_salario = None
menor_salario = None

opcao = ""

while opcao != "2":
  print("\n=== PESQUISA MUNICIPAL ===")
  print("1 – Adicionar família")
  print("2 – Sair e exibir resultados")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    salario = float(input("Digite o salário da família: R$ "))
    filhos = int(input("Digite o número de filhos: "))

    total_familias += 1
    soma_salario += salario
    soma_filhos += filhos

    if maior_salario is None or salario > maior_salario:
      maior_salario = salario

    if menor_salario is None or salario < menor_salario:
      menor_salario = salario

  elif opcao == "2":
    print("\n=== RESULTADOS DA PESQUISA ===")
    if total_familias > 0:
      media_salario = soma_salario / total_familias
      media_filhos = soma_filhos / total_familias

      print(f"Total de famílias: {total_familias}")
      print(f"Média de salário: R$ {media_salario:.2f}")
      print(f"Média de filhos: {media_filhos:.1f}")
      print(f"Maior salário: R$ {maior_salario:.2f}")
      print(f"Menor salário: R$ {menor_salario:.2f}")
    else:
      print("Nenhuma família foi cadastrada.")

  else:
    print("Opção inválida! Digite 1 ou 2.")