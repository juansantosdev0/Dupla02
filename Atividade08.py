import os 
os.system("cls")


login_cadastrado = input("Cadastre o seu login: ")
senha_cadastrada = input("Cadastre a sua palavra-passe: ")

tentativas = 0

while tentativas < 3:
  login = input("Digite o login: ")
  senha = input("Digite a palavra-passe: ")

  if login == login_cadastrado and senha == senha_cadastrada:
    print("Seja bem-vindo(a) ao portal da Clínica VidaPlena!")
    break

  tentativas += 1
  print("Login ou palavra-passe incorretos.")

if tentativas == 3:
    print("Acesso bloqueado por exceder 3 tentativas incorretas.")