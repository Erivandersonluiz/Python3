import logging

logging.basicConfig(filename='operacao_matematicas.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


def soma(*args):
    s = sum(args)
    #print(f'soma {args} = {s}')
    logging.debug(f'soma {args} = {s}')
    return s

def media(*args):
    m = sum(args)/len(args)
    #print(f'media {args} = {m}')
    logging.debug(f'media {args} = {m}')

    return m 

def divisao(*args):
    # Multiplos numeros em (a,b) de forma tal que a/b
    resultados = []
    for ab in args:
        for a,b in ab:
            resultados.append(a/b)
    #print(f'divisao {args} = {resultados}')
    logging.debug(f'divisao {args} = {resultados}')

    return resultados

soma(23,85,41,10) 

media(5,6,7,9,2,3,1)

divisao([(5,6), (8,4), (9,3)])
