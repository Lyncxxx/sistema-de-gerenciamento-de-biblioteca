from random import randint

def cabecalho(msg):
    tamanho_da_msg = len(msg)+4
    print('-'* tamanho_da_msg)
    print(msg)
    print('-' * tamanho_da_msg)

def valida_int(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Informe um numero inteiro válido.')
        else:
            return n

def valida_isnb(msg):
    while True:
        isnb = str(input(msg)).strip()
        if len(isnb) == 9 and isnb[7] == '-' and isnb[0:6].isnumeric() and isnb[8].isnumeric():
            return isnb
        else:
            print('ERRO! Informe um isnb válido!')

def valida_resposta(msg):
    while True:
        res = str(input(msg)).strip().lower()[0]
        if res in 'sn':
            return res
        else:
            print('ERRO! Informe uma opção válida(tente sim ou não).')

def gerar_id():
    id = randint(1000, 9000)
    return id

def gerar_isbn():
    primeira_parte = str(randint(1_000_000, 9_000_000))
    segunda_parte = str(randint(0, 9))
    isbn = primeira_parte + '-' + segunda_parte
    return isbn
