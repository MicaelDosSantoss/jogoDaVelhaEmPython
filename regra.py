from jogo import jogo
from Escolha import Escolhido,rival



def regra(Escolhido,rival):

    for i in range(9):
        jogo(i)

    
        selecao = int(input('Escolha um numero de 1 a 9: '))

        if 1 <= selecao <= 9:
            print('certo')

        else:
            while True:
                selecao = int(input('Numero invalido, digite novamente. \n Escolha um numero de 1 a 9: '))

                if 1 <= selecao <= 9:
                    print('certo')
                    break
        
        
        if selecao == 1:
            jogo[0].value = Escolhido 






regra(Escolhido,rival)