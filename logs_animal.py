import logging

# Coloca como aquivo FILENAME antes do level 
# dentro do parentes vc coloca level= .. para definir o level do log
logging.basicConfig(filename='animal.log', 
                    level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        # aqui antes tinha um PRINT mas foi substituido pelo LOGGING
        #print(f'Animal de nome "{self.nome}" e tipo "{self.tipo}" Criado!') 

        # level do log INFO
        logging.info(f'Animal de nome "{self.nome}" e tipo "{self.tipo}" Criado!')
        
        # level do log warning 
        #logging.warning(f'Animal de nome "{self.nome}" e tipo "{self.tipo}" Criado!') 


cao = Animal('Branco', 'canino')
gato = Animal('lupita', 'felino')
