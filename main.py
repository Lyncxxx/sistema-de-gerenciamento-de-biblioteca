import sys
from random import randint


def gerar_id():
    id = randint(1000, 9000)
    return id

class Livro:
    def __init__(self, titulo, autor, isnb):
        self.titulo = titulo
        self.autor = autor
        self.isnb = isnb
        self.status = 'Disponível'

    def __str__(self):
        return f'''TÍTULO: {self.titulo}
AUTOR: {self.autor}
STATUS: {self.status}'''

    def esta_disponivel(self):
        if self.status == 'Disponível':
            return True
        else:
            return False

    def alterar_status(self, novo_status):
        if novo_status == self.status:
            print('ERRO! Novo status igual ao atual.')
        else:
            self.status = novo_status
            print('Status alterado com sucesso!')

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id_de_usuario = gerar_id()
        self.livros_emprestados = []
        self.limite_de_emprestimos = 3

    def __str__(self):
        return f'''Nome: {self.nome} 
ID de Usuário: {self.id_de_usuario}'''

    def requisitar_livro(self, livro):
        self.livros_emprestados.append(livro)
        self.limite_de_emprestimos -= 1
        print('Livro emprestado com sucesso!')

    def devolver_livro(self, livro):
        self.livros_emprestados.remove(livro)
        self.limite_de_emprestimos += 1
        print('Livro devolvido com sucesso!')

    def exibir_livros_emprestados(self):
        if len(self.livros_emprestados) > 0:
            for livro in self.livros_emprestados:
                print(livro)
        else:
            print('Você não tem livro emprestados.')

class Biblioteca:
    def __init__(self):
        self.catalogo_de_livros = []
        self.lista_de_usuarios = []

    def adicionar_livro(self, livro):
        self.catalogo_de_livros.append(livro)
        print('Livro adicionado ao catalgo com sucesso!')

    def remover_livro(self, livro):
        self.catalogo_de_livros.remove(livro)
        print('Livro removido do catalogo com sucesso!')

    def emprestar_livro(self, usuario, livro):
        livro.alterar_status('Emprestado')
        usuario.requisitar_livro(livro)


    def devolver_livro(self, usuario, livro):
        livro.alterar_status('Disponível')
        usuario.devolver_livro(livro)

    def pesquisar_titulo(self):
        ...

    def pesquisar_autor(self):
        ...

    def exibir_livros(self):
        for livro in self.catalogo_de_livros:
            print(livro)

    def adicionar_usuario(self):
        nome = input('Informe o nome: ')
        novo_usuario = Usuario(nome)
        self.lista_de_usuarios.append(novo_usuario)
        print('Novo usuário cadastrado com sucesso!')

    def exbir_usuarios(self):
        if len(self.lista_de_usuarios) == 0:
            print('Nenhum usuário cadastrado!')
        for usuario in self.lista_de_usuarios:
            print(usuario)



biblioteca = Biblioteca()
livro1 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1)
livro2 = Livro('Romeu E Julieta', 'William Shakespeare', 2)
livro3 = Livro('1984', 'George Orwell', 3)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

while True:
    opcao = int(input('''[1] EMPRESTIMO
[2] DEVOLUCÃO
[3] LISTAR LIVROS
[4] LISTAR USUÁRIOS
[5] FILTRAR LIVROS
[6] ADICIONAR LIVRO
[7] REMOVER LIVROS
> '''))
    if opcao == 1 or opcao == 2:
        user_encotrado = False
        livro_encontrado = False
        user_id = int(input('Informe o ID do usuário: '))
        isnb_livro = int(input('Informe o ISNB do livro: '))
        for usuario in biblioteca.lista_de_usuarios:

            if usuario.id_de_usuario == user_id:
                user_encotrado = True
                for livro in biblioteca.catalogo_de_livros:

                    if livro.isnb == isnb_livro:
                        livro_encontrado = True

                        if opcao == 1 and livro.esta_disponivel():
                            biblioteca.emprestar_livro(usuario, livro)
                        elif opcao == 2:
                            biblioteca.devolver_livro(usuario, livro)

                if not livro_encontrado:
                    print('ERRO! Livro não encotrado!')

        if not user_encotrado:
            print('ERRO! Usuário não encontrado.')
            res = input('Gostaria de cadastra-lo? [s/n]').lower().strip()[0]
            if res == 's':
                biblioteca.adicionar_usuario()

    elif opcao == 3:
        biblioteca.exibir_livros()

    elif opcao == 4:
        biblioteca.exbir_usuarios()

    elif opcao == 5:
        pass

    elif opcao == 6:
        sys.exit()
