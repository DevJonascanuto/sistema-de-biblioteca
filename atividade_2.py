import matplotlib.pyplot as plt

# Classe Livro incluido boas praticas, primeira letra da class em maiuscula
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"


# Lista de livros
biblioteca = []


#  criando as Funções do sistema
def cadastrar_livros():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    genero = input('Digite o gênero do livro: ')
    quantidade = int(input('Digite a quantidade disponível: '))

    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f" O livro {novo_livro} foi cadastrado com sucesso!")


def listar_livros():  # essa função lista os livros cadastrados
    if not biblioteca:
        print(" Nenhum livro cadastrado.")
    else:
        print("\n--- LISTA DE LIVROS ---")
        for l in biblioteca:
            print(l)


def buscar_livro():  # essa função busca o livro de acordo com o titulo , poderiamos usar um id tambem para a busca
    titulo_busca = input('Digite o título do livro que deseja buscar: ')
    encontrados = [l for l in biblioteca if l.titulo.lower() == titulo_busca.lower()]
    if encontrados:
        print(" Livro encontrado:")
        for l in encontrados:
            print(l)
    else:
        print(" Livro não encontrado.")


def gerar_grafico(): # função que gera o grafico de acordo com o genero 
    if not biblioteca:
        print(" Nenhum livro cadastrado para gerar gráfico.")
        return

    generos = {}
    for l in biblioteca:
        generos[l.genero] = generos.get(l.genero, 0) + l.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Quantidade de Livros por Gênero")
    plt.show()


# Menu principal
def menu():
    while True:
        print('\n===== MENU BIBLIOTECA =====')
        print('1 - Cadastrar livro')
        print('2 - Listar todos os livros')
        print('3 - Buscar livro por título')
        print('4 - Gerar gráfico por gênero')
        print('0 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_livros()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            gerar_grafico()
        elif opcao == '0':
            print(' Sistema encerrado.')
            break
        else:
            print(' Opção inválida. Tente novamente.')


menu()
