import os
os.system('cls')

renda = float(input('Digite sua renda mensal: '))
emprestimo = float(input('Quanto gostaria de emprestimo? '))
prestacoes = int(input('Em quantas prestações deseja pagar? '))

prestacao = emprestimo / prestacoes

print(f'Valor da prestação mensal: R$ {prestacao:.2f}')

if emprestimo <= renda * 10 and prestacao <= renda * 0.30:
    print('Aprovado!')
else:
    print('Negado, tente novamente!')
