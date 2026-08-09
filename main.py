import definicoes as d # Importa as funções de limpar a tela e o cabeçalho que estão em outro arquivo.
d.limpa()
d.cabecalho()

lista_de_livros = [] # Essa lista guardará todos os livros cadastrados no sistema.

def cadastrar(titulo, autor, publicacao, codigo_isbn):
    novo_livro = {  # Cria o dicionário do livro cadastrado com as informações fornecidas.
        "titulo": titulo.title(), # O .title() deixa as primeiras letras maiúsculas, para padronizar a escrita e deixar mais organizado.
        "autor": autor.title(),
        "publicacao": publicacao,
        "isbn": codigo_isbn,
        "status": "disponível" } # Todo livro que acaba de ser cadastrado começa disponível.
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

while True: # Mantém o menu principal rodando continuamente até o usuário escolher a opção 7 para sair.
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
        while True:
            publicacao = input("Digite o ano de publicação: ")
            if publicacao.isdigit() and len(publicacao) == 4: # Verifica se o ano digitado é válido (apenas números e 4 dígitos).
                break # Se a data for válida, sai da repetição, senão continua até que seja válida.
            else:
                print("\nO ano de publicação digitado é inválido. Tente novamente.")
        while True:
            codigo_isbn = input("Digite o Código ISBN com os traços (ex: 012-34-567-8910-1): ")
            codigo_isbn = codigo_isbn.replace(" ", "")
            codigo_teste = codigo_isbn.replace("-", "") # Cria uma cópia temporária e usa o .replace() para remover os traços e espaços.
            if len(codigo_teste) == 13 and codigo_teste.isdigit() and codigo_isbn.count("-") == 4: # Verifica se o código digitado tem 13 números e 4 hífens.
                break # O loop continuará até que o código digitado seja válido.
            else:
                print("\nO código ISBN digitado é inválido. Tente novamente.")
        novo_livro = cadastrar(titulo, autor, publicacao, codigo_isbn) # Chama a função cadastrar() para criar o dicionário do livro com as informações fornecidas no input.
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