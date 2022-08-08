



def soma(*args):
    s = sum(args)
    print(f'suma {args} = {s}')
    return s

def media(*args):
    m = sum(args)
    print(f'media {args} = {m}')
    return m 

def divisao(*args):
    # Multiplos numeros em (a,b) de forma tal que a/b
    resultados = []
    for ab in args:
        for a,b in ab:
            resultados.append(a/b)
    print(f'divisao {args} = {resultados}')
    return resultados

soma(23,85,41,10) 

media(5,6,7,9,2,3,1)

divisao([(5,6), (8,4), (9,3)])