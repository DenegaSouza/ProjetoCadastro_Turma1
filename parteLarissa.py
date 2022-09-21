"""2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre 
finalizar o suporte ou conversar com um atendente."""

from datetime import datetime
import random


#ISSO AQUI EU CRIEI PARA CONSEGUIR

nome = str(input("Digite o seu nome: ")).title()
cpf = int(input("Digite o seu CPF: "))
telefone = input("Digite o seu telefone: ")
protocolo = random.randint(0,10000000000)


escolha_1 = int(input("O que você quer fazer? \n1- Reclamação\n2- Alteração de Dados\n"))

while escolha_1 == 1:
    reclamacao = str(input("Qual a sua reclamação? "))
    print(f"Obrigado(a) {nome} pelas informações fornecidas! O seu protocolo é o número {protocolo}\nIremos avaliar e entraremos em contato no telefone informado.")

    escolha_1 = str(input("Deseja finalizar o atendimento ou conversar com um atendente? Escolha: \n1- Finalizar atendimento.\n2- Conversar com um atendente\n"))
    break

else:
    str(input("Qual dados você gostaria de alterar? "))

print("Obrigada por ter nos escolhido!")

