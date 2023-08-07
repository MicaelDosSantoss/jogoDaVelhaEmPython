

def restricao(pergunta):
    
    if 1 <= pergunta <= 9:
        return pergunta
    else:
        while True:
            pergunta = int(input('Numero invalido, digite novamente. \n Escolha um numero de 1 a 9: '))

            if 1 <= pergunta <= 9:
                return pergunta
                break              

           

