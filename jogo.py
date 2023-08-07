
from Escolha import Escolhido, rival
from rival import rivals
from restricao_de_escolha import restricao
# from restricao_de_escolha import restricaoEscolha

color_green = '\033[32m'
color_puple = '\033[35m'
close_color = '\033[0m'


n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9


def marcacao(n1,n2,n3,n4,n5,n6,n7,n8,n9):

    for i in range(6): 

        print(f'\n {n1} | {n2} | {n3} \n {n4} | {n5} | {n6} \n {n7} | {n8} | {n9} \n')

        pergunta = int(input(f'Escolha um dos números acima: '))

        restricao(pergunta)
        
        if Escolhido == 'X':

            if pergunta == n1:
                str(n1)
                n1 = f'{color_green}{Escolhido}{close_color}'

            if pergunta == n2:
                str(n2)
                n2 = f'{color_green}{Escolhido}{close_color}'
            
            if pergunta == n3:
                str(n3)
                n3 = f'{color_green}{Escolhido}{close_color}'
            
            if pergunta == n4:
                str(n4)
                n4 = f'{color_green}{Escolhido}{close_color}'
            
            if pergunta == n5:
                str(n5)
                n5 = f'{color_green}{Escolhido}{close_color}'

            if pergunta == n6:
                str(n6)
                n6 = f'{color_green}{Escolhido}{close_color}'
            
            if pergunta == n7:
                str(n7)
                n7 = f'{color_green}{Escolhido}{close_color}'
            
            if pergunta == n8:
                str(n8)
                n8 = f'{color_green}{Escolhido}{close_color}'

            if pergunta == n9:
                str(n9)
                n9 = f'{color_green}{Escolhido}{close_color}'
    
    rivals(rival)
       
       
        


marcacao(n1,n2,n3,n4,n5,n6,n7,n8,n9)