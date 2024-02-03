'''
O computador vai pensar em um número de 0 e 10. O jogador vai tentar adivinhar 
até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

import random
from time import sleep

# Título do Jogo
print('=' * 50)
msg = 'Jogo da Adivinhação!'
print(f'{msg:^50}')
print('=' * 50)

acertou = False
tentativas = 0

# Gerando escolha do computador
x = random.randint(0, 10)

while acertou == False:
   
    n = int(input('Tente advinhar um número de 0 a 10: '))

    print('Processando...')
    sleep(0.5)
    
    if n > 10:
        print('\nOpção inválida')
    elif n == x:
        print(f'\nPensei no número {x}, acertou!')
        acertou = True
        tentativas += 1
    else:
        print(f'\nErrou, tente mais uma vez.')
        tentativas += 1

# Score final
print(f'\nNúmero de tentativas: {tentativas}')
