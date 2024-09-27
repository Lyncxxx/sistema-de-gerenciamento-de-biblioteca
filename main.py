import sys
from random import randint
from time import sleep



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

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.isnb = gerar_isbn()
        self.status = 'Disponível'

    def __str__(self):
        return f'{self.titulo:<28} {self.autor:<25} {self.isnb:>15} {self.status:>15}'

    def esta_disponivel(self):
        if self.status == 'Disponível':
            return True


    def alterar_status(self, novo_status):
        if novo_status == self.status:
            print('ERRO! Novo status igual ao atual.')
        else:
            self.status = novo_status

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id_de_usuario = gerar_id()
        self.livros_emprestados = []
        self.total_de_imprestimos = 0

    def __str__(self):
        return f'''{self.nome:<28} {self.id_de_usuario:<15} {self.total_de_imprestimos:>10}'''

    def requisitar_livro(self, livro):
        if self.total_de_imprestimos < biblioteca.limite_de_emprestimos:
            self.total_de_imprestimos += 1
            self.livros_emprestados.append(livro)
            print('Livro emprestado com sucesso!')
        else:
            print('ERRO! Usuario excedeu o limite total de emprestimos.')

    def devolver_livro(self, livro):
        self.total_de_imprestimos -= 1
        self.livros_emprestados.remove(livro)
        print('Livro devolvido com sucesso!')

    def exibir_livros_emprestados(self):
        if len(self.livros_emprestados) > 0:
            for livro in self.livros_emprestados:
                print(livro)
        else:
            print('Você não tem livro emprestados.')

class Biblioteca:
    limite_de_emprestimos = 3
    livro_encontrado = usuario_encontrado = False
    def __init__(self):
        self.catalogo_de_livros = []
        self.lista_de_usuarios = []

    def adicionar_livro(self):
        titulo = str(input('Título: '))
        autor = str(input('Autor: '))
        novo_livro = Livro(titulo, autor)
        self.catalogo_de_livros.append(novo_livro)
        print('Livro adicionado ao catalogo com sucesso!')

    def remover_livro(self):
        isbn = valida_isnb('Informe o ISBN do livro a ser removido: ')
        for livro in self.catalogo_de_livros:
            if livro.isnb == isbn:
                self.catalogo_de_livros.remove(livro)
                print('Livro removido do catalogo com sucesso!')

    def emprestar_livro(self, user_id, isnb_livro):
        for usuario in self.lista_de_usuarios:
            if user_id == usuario.id_de_usuario:
                biblioteca.usuario_encontrado = True
                for livro in self.catalogo_de_livros:
                    if livro.isnb == isnb_livro:
                        if livro.esta_disponivel():
                            biblioteca.livro_encontrado = True
                            livro.alterar_status('Emprestado')
                            usuario.requisitar_livro(livro)
                        else:
                            print('ERRO! Livro indisponível para emprestimo.')
        if not biblioteca.livro_encontrado or not biblioteca.usuario_encontrado:
            print('ERRO! ID de usuário ou ISNB inválidos.')


    def devolver_livro(self, id, isnb):
        for usuario in self.lista_de_usuarios:
            if usuario.id_de_usuario == id:
                biblioteca.usuario_encontrado = True
                for livro in self.catalogo_de_livros:
                    if livro.isnb == isnb:
                        biblioteca.livro_encontrado = True
                        if livro.esta_disponivel():
                            print('ERRO! Livro já consta como devolvido.')
                        else:
                            livro.alterar_status('Disponível')
                            usuario.devolver_livro(livro)
        if not biblioteca.livro_encontrado or not biblioteca.usuario_encontrado:
            print('ERRO! ID de usuário ou ISNB inválidos.')

    def pesquisar_titulo(self):
        contador = 0
        titulo_pesquisado = str(input('Insira o título a ser filtrado: ')).strip().title()
        cabecalho(f'{'TÍTULO':<28} {'AUTOR':<25} {'ISNB':>10} {'STATUS':>16}')
        for livro in self.catalogo_de_livros:
            if titulo_pesquisado in livro.titulo:
                contador += 1
                print(livro)
        if contador == 0:
            print('ERRO! Não há nenhum livro com a título informada.')
        print('-' * 86)

    def pesquisar_autor(self):
        contador = 0
        autor_pesquisado = str(input('Insira o autor a ser filtrado: ')).strip().title()
        cabecalho(f'{'TÍTULO':<28} {'AUTOR':<25} {'ISNB':>10} {'STATUS':>16}')
        for livro in self.catalogo_de_livros:
            if autor_pesquisado in livro.autor:
                contador += 1
                print(livro)
        if contador == 0:
            print('Não há nenhum livro com o autor informado.')
        print('-' * 86)

    def exibir_livros(self):
        cabecalho(f'{'TÍTULO':<28} {'AUTOR':<25} {'ISNB':>10} {'STATUS':>16}')
        for livro in self.catalogo_de_livros:
            print(livro)
        print('-' * 86)

    def adicionar_usuario(self):
        nome = input('Informe o nome: ').title().strip()
        novo_usuario = Usuario(nome)
        self.lista_de_usuarios.append(novo_usuario)
        print(f'{novo_usuario.nome} foi cadastrado com sucesso. Seu ID é {novo_usuario.id_de_usuario}')


    def exbir_usuarios(self):
        cabecalho(f'{'NOME':<28} {'ID DE USUÁRIO':<23} {'N° EMPRESTIMOS':>15}')
        if len(self.lista_de_usuarios) == 0:
            print('Nenhum usuário cadastrado!')
        else:
            for usuario in self.lista_de_usuarios:
                print(usuario)
        print('-' * 73)

biblioteca = Biblioteca()
livro1 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry')
livro2 = Livro('Romeu E Julieta', 'William Shakespeare')
livro3 = Livro('1984', 'George Orwell')
livro4 = Livro('Dom Casmurro', 'Machdo de Assis')
livro5 = Livro('As Crônicas De Nárnia', 'C.S Lewis')
usuario1 = Usuario('Maria Joana')
usuario2 = Usuario('João da Silva')
usuario3 = Usuario('Marcos Felipe')
biblioteca.catalogo_de_livros.extend([livro1, livro2, livro3, livro4, livro5])
biblioteca.lista_de_usuarios.extend([usuario1, usuario2, usuario3])

while True:
    opcao = valida_int('''
MENU
[1] EMPRESTIMO
[2] DEVOLUCÃO
[3] LISTAR LIVROS
[4] LISTAR USUÁRIOS
[5] FILTRAR LIVROS
[6] ADICIONAR LIVRO
[7] REMOVER LIVRO
[8] SAIR
> ''')
    if opcao == 1 or opcao == 2:
        if opcao == 1:
            res = valida_resposta('O usuário já possui cadastro? [s/n]')
            if res == 'n':
                biblioteca.adicionar_usuario()
        user_id = valida_int('Informe o ID do usuário: ')
        while True:
            isnb_livro = valida_isnb('Informe o ISNB do livro: ')
            if opcao == 1:
                biblioteca.emprestar_livro(user_id, isnb_livro)
            else:
                biblioteca.devolver_livro(user_id, isnb_livro)

            mais_livros = valida_resposta('Mais algum outro livro?[s/n] ')
            if mais_livros == 'n':
                break


    elif opcao == 3:
        biblioteca.exibir_livros()

    elif opcao == 4:
        biblioteca.exbir_usuarios()

    elif opcao == 5:
        opcao_filtragem = valida_int('''[1] FILTRAR POR TÍTULO
[2] FILTRAR POR AUTOR
> ''')
        if opcao_filtragem == 1:
            biblioteca.pesquisar_titulo()
        elif opcao_filtragem == 2:
            biblioteca.pesquisar_autor()
        else:
            print('ERRO! Informe uma opção válida(tente um número entre 1 e 2)!')

    elif opcao == 6:
        biblioteca.adicionar_livro()

    elif opcao == 7:
        biblioteca.remover_livro()

    elif opcao == 8:
        print('Saindo', end='')
        for c in range(3):
            sleep(1)
            print('. ', end='')
        sys.exit()

    else:
        print('ERRO! Informe uma opção válida(tente um número entre 1 e 8).')