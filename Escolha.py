
print('{}\n "\033[35m JOGO DA VELHA \033[0m" \n{}'.format('='*20,'='*20))

Escolhido = input('Você deseja \033[1mO\033[0m ou \033[1mX\033[0m : ')


while True:  

    if Escolhido == 'X' or Escolhido == 'x':
        Escolhido = 'X'
        break

    if Escolhido == 'O' or Escolhido == 'o':
        Escolhido = 'O' 
        break

    else: 
        Escolhido = input('Valor invalido, digite novamente: ')
        
        if Escolhido == 'X' or Escolhido == 'x':
            Escolhido = '\033[32mX\033[0m'
            break

        if Escolhido == 'O' or Escolhido == 'o':
            Escolhido = '\033[35mO\033[m'
            break

rival = ''

if Escolhido == 'X':
    rival = 'O'
if Escolhido == 'O':
    rival = 'X'

if rival == 'O' and Escolhido == 'X':
    print(f'Voce escolheu \033[32m{Escolhido}\033[0m')
    print(f'O Rival escolheu \033[35m{rival}\033[m')
if rival == 'X' and Escolhido == 'O':
    print(f'Você esolheu \033[35m{Escolhido}\033[0m')
    print(f'O Rival escolheu \033[32m{rival}\033[m')
