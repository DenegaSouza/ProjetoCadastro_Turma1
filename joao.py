'''3- Se ele escolher falar com atendente deverá entrar na fila de espera'''

import os
import time
import random

escolha = 'Atendente'
atendente = ['Xuxa', 'Shakira', 'Faustão', 'Ana Maria Braga']

if escolha == 'Atendente': #se for escolhido falar com atendente, inicia o código
    for x in range(10, 0, -1):
        os.system('cls')
        print(f'Você está na posição {x}') #diz a posição
        time.sleep(random.randint(0,5)) #possui intervalo aleatório entre uma posição e outra
    os.system('cls')
    print('Erro no sistema!\nEstamos reiniciando...')
    time.sleep(3)
    for x in range(random.randint(9,15), 0, -1): #a posição é aleatória entre 9 e 15
        os.system('cls')
        print(f'Você está na posição {x}') #diz a posição
        time.sleep(random.randint(0,5)) #possui intervalo aleatório entre uma posição e outra
    os.system('cls')
    print("Atendente {} irá te recepcionar!".format(random.choice(atendente))) #um atendente aleatório da lista será chamado