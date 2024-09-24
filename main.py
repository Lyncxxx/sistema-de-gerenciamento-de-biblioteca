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

    def emprestar_livro(self, usurio, livro):
        ...

    def devolver_livro(self):
        ...

    def pesquisar_titulo(self):
        ...

    def pesquisar_autor(self):
        ...

    def adicionar_usuario(self, usuario):
        self.lista_de_usuarios.append(usuario)

    def exbir_usuarios(self):
        for usuario in self.lista_de_usuarios:
            print(usuario)




livro1 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1)
livro2 = Livro('Romeu E Julieta', 'William Shakespeare', 2)
livro3 = Livro('1984', 'George Orwell', 3)
usuario1 = Usuario('Maria Paula')
usuario2 = Usuario('Ana Julia')
usuario3 = Usuario('Maria Cristina')

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)
biblioteca.adicionar_usuario(usuario3)



while True:
    opcao = int(input('''[1] EMPRESTIMO
[2] DEVOLUCÃO
[3] LISTA DE LIVROS
[4] LISTA DE USUÁRIOS
[5] PESQUISAR LIVROS
> '''))
    if opcao == 1:
        biblioteca.emprestar_livro()

    if opcao == 4:
        biblioteca.exbir_usuarios()
