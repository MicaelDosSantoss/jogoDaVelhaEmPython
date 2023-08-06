
def jogo(i):

    print('{}\n \033[1m{}\033[0m RODADA \n{}'.format('='*20,i+1,'='*20))

    n1 = 1
    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6
    n7 = 7
    n8 = 8
    n9 = 9

    print(f'\n {n1} | {n2} | {n3} ')
    print(f' {n4} | {n5} | {n6} ')
    print(f' {n7} | {n8} | {n9} \n')

    return [n1, n2, n3, n4, n5, n6, n7, n8, n9]