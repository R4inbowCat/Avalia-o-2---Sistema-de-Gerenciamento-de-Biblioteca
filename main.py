import definicoes as d
d.limpa()
d.cabecalho()

lista_de_livros = [] # Essa lista guardará todos os livros cadastrados no sistema.

def cadastrar(titulo, autor, publicacao, codigo_isbn):
    novo_livro = {  # Cria o dicionário do livro cadastrado com as informações fornecidas.
        "Título": titulo,
        "Autor": autor,
        "Publicação": publicacao,
        "Código ISBN": codigo_isbn,
        "Status": "Disponível" } # Todo livro que acaba de ser cadastrado começa disponível.
    return novo_livro

def emprestimo():
    pass
def devolucao():
    pass
def listar():
    pass
def ordenar():
    pass
def buscar():
    pass

while True:
    print("========================================")
    print(" Sistema de Gerenciamento de Biblioteca")
    print("========================================")
    print("● 1. Cadastrar livro")
    print("● 2. Registrar empréstimo")
    print("● 3. Registrar devolução")
    print("● 4. Listar livros")
    print("● 5. Ordenar a listagem")
    print("● 6. Buscar livro")
    print("● 7. Sair do programa")
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        titulo = input("\nDigite o título do livro: ")
        autor = input("Digite o autor: ")
        publicacao = input("Digite o ano de publicação: ")
        codigo_isbn = input("Digite o Código ISBN: ")
        novo_livro = cadastrar(titulo, autor, publicacao, codigo_isbn)
        lista_de_livros.append(novo_livro) # Adiciona o dicionário do livro na lista de livros cadastrados.
        print("\nLivro cadastrado com sucesso!")
    elif opcao == 2:
        emprestimo()
    elif opcao == 3:
        devolucao()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        ordenar()
    elif opcao == 6:
        buscar()
    elif opcao == 7:
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida, tente novamente.")