
from datetime import date
from random import randint
import os
import time
import random



"""
O intuito é fazer um chatbot de suporte técnico.          

1- Primeiramente terá um menu questionando ao usuário se ele quer se identificar ou não (reclamar de forma anônima)
- Se ele escolher se identificar, o usuário deve informar seu nome, CPF e telefone.

2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre
finalizar o suporte ou conversar com um atendente.

3- Se ele escolher falar com atendente deverá entrar na fila de espera

4- Se ele escolher alterar dados, o usuário deverá escolher qual dado quer alterar
- No caso dele alterar algum dado, as informações do usuário que estarão salva num dicionário deverão ser
atualizadas pelo programa.

5 - No caso da alteração do cpf, o programa deverá informar se o dado digitado pelo usuário é um valor de cpf válido.

1 - No caso de ser anônimo, o usuário vai direto pra parte de reclamar (já que não tem dado pra ser verificado ou coisa do tipo)"""


# MENSAGEM DE INÍCIO DO BOT E CONFIRMACAO DE IDENTIFICACAO
id = str(input("BEM-VINDO(A) AO CHATBOT!\nPor favor, digite SIM para se identificar ou NÃO para continuar: "))


# SOLICITACAO DE DADOS DO USUARIO.
if id == "sim":
    print("\nPara darmos seguimento tenha em mãos os seguintes dados: Nome completo, número de CPF e telefone")
    nome = str(input("Agora, por favor informe seu nome: "))
    

    #### INCLUIR VERIFICAÇÃO DE VALIDADE DO CPF ####
    # VALIDADOR DE CPF

# LISTAS
rLista = list()             # Respostas dos cálculos
listaCPF = list()           # Lista do CPF fracionado em str
listaInt = list()           # LIsta do CPF fracionado em int

# CPF deve ser salvo como STR porque caso inicie com '0' irá dar erro ao salvar no dicionário

while True :
        # VARIÁVEIS
        decrescente = 10
        posicao = 0
        listaCPF.clear()
        rLista.clear()
        listaInt.clear()
        cpf = input(f"Obrigado, {nome}! Agora precisamos de seu CPF. Digite apenas os números, sem pontuação: ").strip()
        cpf = cpf.replace('.', '')              # REMOÇÃO DE '.' E '-'
        cpf = cpf.replace('-', '')

        if len(cpf) != 11 or not cpf.isdecimal():   # se CPF for diferente de 11 e se não for decimal
            print('Digite o CPF corretamente!\n')   #Se digitar a quantidade de números errada

        else:
            listaCPF = list(cpf)    #CPF AINDA É UMA str FOI FATIADO NA LISTA

            # PRIMEIRO DIGITO

            # PADRÃO
            """
            for c in range(0, len(listaCPF)):
                listaInt.append(int(listaCPF[c]))       # CPF NA LISTA INT
            """
            # FIM PADRÃO

            [listaInt.append(int(digito)) for digito in listaCPF]     # LIST COMPREHENSION

            for c in range(10, 1, -1):
                """
                Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente
                de números de 10 à 2 e soma os resultados
                """
                rLista.append(listaInt[posicao]*c)   # c=10,9,8,7...  posicao=0,1,2,3,4...
                posicao += 1        # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int
                                    # EU NÃO CONSEGUI FAZER ISSO SEM USAR DUAS LISTAS

            # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
            # Caso resto da divisão = 10, considerar = 0
            # Se o resultado for igual ao primeiro digito do cpf (posição 9) , primeira parte da validação OK

            resultado = (sum(rLista)*10 ) % 11
            if resultado == 10:
                resultado = 0

            #print(resultado)   Teste para ver se o resultado é igual ao penultimo digito

            if resultado == listaInt[-2] and len(set(listaInt)) > 1:     # IRÁ PROCEGUIR CASO PASSE A PRIMEIRA VALIDAÇÃO
                                                                        # SET() REMOVE OS ITENS DUPLICADOS
                # SEGUNDO DIGITO                                         # CASO O USUÁRIO DIGITE 11111111111
                # VARIÁVEIS
                decrescente = 10
                posicao = 0
                rLista.clear()      # LIMPA rLista

                for c in range(11, 1, -1):
                    """
                    Vamos multiplicar os 10 primeiros números (9 números + 1 digito verificador) pela 
                    sequência decrescente de números de 11 à 2 
                    """
                    rLista.append(listaInt[posicao]*c)   # c=11,9,8,7...  posicao=0,1,2,3,4...
                    posicao += 1        # O RESULTADO ESTÁ SEDO ADICIONADO EM OUTRA LISTA COMO int E NÃO MAIS str
                                        # EU NÃO CONSEGUI FAZER ISSO DE OUTRO JEITO

                # O próximo passo: multiplicar a soma dos resultado por 10. dividir por 11 e pegar apenas o resto da divisão
                # Caso resto da divisão = 10, considerar = 0
                # Se o resultado for igual ao primeiro digito do cpf (posição 10) , primeira parte da validação OK

                resultado = (sum(rLista)*10 ) % 11
                if resultado == 10:
                    resultado = 0

                #print(resultado)           teste para confirmar se o resultado é igual ao ultimo digito

                if resultado == listaInt[-1]:
                    print('CPF ok')         ##*** FAZER A ALTERAÇÃO OU CADASTRO DO CPF AQUI ***##
                    
                break        
                    
            else:
                print('CPF inválido!')
            
        tel = int(input("Excelente, seu CPF é válido! Por último, favor digitar seu telefone para contato com DDD: "))

else:
        print("Ok, vamos continuar conversando sem identificação.")
    ### INCLUIR CADASTRO DA RECLAMACAO AQUI.



"""
2- Após isso, o programa tem que questionar se o usuário quer fazer uma reclamação ou alterar um dado.
- Se ele escolher reclamação, ele deve digitar o que aconteceu, após isso o usuário poderá escolher entre 
finalizar o suporte ou conversar com um atendente.
"""

#AS BIBLIOTECAS QUE PRECISO


#ISSO AQUI EU CRIEI PARA CONSEGUIR FAZER TESTES - NO CÓDIGO VAI PRECISAR TROCAR O NOME DAS VARIÁVEIS


poli = "~"*50

#EU PRECISO DISSO PRO MEU CÓDIGO FUNCIONAR
protocolo = [randint(1,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)]
anoProtocolo = date.today().year
protocolostr = ""
for c in range (0,len(protocolo)):
    protocolostr += str(protocolo[c])       # Transforma em str para ficar sem os [] da lista

#AQUI É O CÓDIGO PROPRIAMENTE DITO:

print(f"{poli}")

escolha_1 = int(input("O que você quer fazer? \n1- Reclamação\n2- Alteração de Dados\nDigite: "))

print(f"{poli}")

while escolha_1 == 1:
    reclamacao = str(input("Qual a sua reclamação? "))
    print(f"{poli}")

    print(f"Obrigado(a) {nome} pelas informações fornecidas! O seu protocolo é o número {protocolostr}-{anoProtocolo}." \
        "\nIremos avaliar e entraremos em contato no telefone informado.")
    
    
    print()

    print(f"{poli}")

    escolha_1 = str(input("Deseja finalizar o atendimento ou conversar com um atendente? Escolha: \n1- Finalizar atendimento." \
        "\n2- Conversar com um atendente\n"))
    break

    print(f"{poli}")

else:
    str(input("Qual dados você gostaria de alterar? "))

# EM TEORIA ACABA AQUI

print(f"{poli}")

print("Obrigada por ter nos escolhido!")        #ISSO FOI SÓ PRA TER ALGO NO FINAL DO MEU CÓDIGO E PODE SAIR.

print(f"{poli}")



'''3- Se ele escolher falar com atendente deverá entrar na fila de espera'''



escolha = 'Atendente'
atendentes = ['Xuxa', 'Shakira', 'Faustão', 'Ana Maria Braga']


if escolha == 'Atendente': #se for escolhido falar com atendente, inicia o código
    for x in range(10, 0, -1):
        os.system('cls')
        print(f'Você está na posição {x}\n*música de fundo*') #diz a posição
        time.sleep(random.randint(0,3)) #possui intervalo aleatório entre uma posição e outra
    os.system('cls')
    print('Erro no sistema!\nEstamos reiniciando...')
    time.sleep(3)
    for x in range(5, 0, -1): #a posição é aleatória entre 9 e 15
        os.system('cls')
        print(f'Você está na posição {x}\n*música de fundo*') #diz a posição
        time.sleep(random.randint(0,3)) #possui intervalo aleatório entre uma posição e outra
        os.system('cls')
        print("Atendente {} irá te recepcionar!".format(random.choice(atendentes))) #um atendente aleatório da lista será chamados
        
    
    print ("Você deseja alterar algum dado? \n Se sim - S \n Se não - N")
    simounao = input()

    

    while simounao == "S":
        lista = [nome, cpf, tel]

        dadoAlterar = str(input("Digite o dado que queira alterar: "))
        dadoNovo = str(input("Digite o novo dado a alterar: "))

        for i in range(len(lista)):
            if lista[i] == dadoAlterar:
                lista[i] = dadoNovo

        for x in range(0, len(lista)):
            print(lista[x])
        print ("Você deseja alterar algum dado novamente? \n Se sim - S \n Se não - N")
        simounao = input()

    print("Você alterou seu dados")


    """
    5 - No caso da alteração do cpf, o programa deverá informar se o dado digitado pelo usuário é um valor de cpf válido. 
    """


    """# VALIDADOR TELEFONE

    dadosCadastro = [{'nome': 'Marcos Silveira', 'cpf': '78946667945'}] # serão salvos em uma lista, cada usuário terá um dicionário dentro da lista
    listaTemp = list()               # lista temporária para conversão de STR > INT

    while True:
        listaTemp.clear()       # sempre irá limpar a lista temporária antes de cadastrar outro usuário
        telefone = str(input('telefone: ')).strip()                   # recebe os dados (telefone) como STR
        telefone = telefone.replace('.', '')                          # REMOÇÃO DE '.' , ' ' E '-' caso o usuário use
        telefone = telefone.replace('-', '')
        telefone = telefone.replace(' ', '')

        if len(telefone) != 11 or not telefone.isdecimal():     # se telefone for diferente de 11 e se não for decimal
            print('Digite um número válido!\n')   #Se digitar a quantidade de números errada correto: 47 98888-7777

        else:
            listaTemp = list(telefone)          # Adiciona o telefone a uma lista ex: [3, 5, 6, 5]
            listaTemp.insert(2, ' ')            # Insere o espaço apos o "DDD"
            listaTemp.insert(8, '-')            # Insere o "-" no meio do número
            telefone = ''.join(listaTemp)       # Junta a lista novamente e passa ela para a variável
            print(telefone)         # print p teste

            # ADICINANDO O NÚMERO PARA O DICIONÁRIO
            dadosCadastro[0]['telefone'] = telefone         # O cadastro estará dentro de um loop
            break                                           # O "0" será o "c" do loop
                                                            # Quando cadastrar outro usuário, o "c" altera sozinho
                                                            # e não precisa se preocupar com a posição da lista

    print(dadosCadastro)    # print p teste

    # FIM VALIDADOR DE TELEFONE"""



    # FIM VALIDADOR CPF
