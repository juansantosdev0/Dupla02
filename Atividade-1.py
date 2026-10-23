import os
os.system('cls')

print('Solicitando Dados')

while True:
    n1 = float(input('Digite seu primeiro numero: '))
    n2 = float(input('Digite seu segundo numero: '))
    op = input('Digite sua operação: ')

    match op:
        case '+':
            print(f'{n1+n2}')
        case '-':
            print(f'{n1-n2}')
        case '*':
            print(f'{n1*n2}')
        case '/':
            print(f'{n1/n2}')
        case _:
            print('Inválido, tente novamente')

    pergunta = str(input('Deseja fazer outro calculo? (S ou N): ')).lower()

    match pergunta:
        case 'S':
            continue
        case 'N':
            break