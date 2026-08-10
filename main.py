import definicoes as d # Importa as funções de limpar a tela e o cabeçalho que estão em outro arquivo.
d.limpa()
d.cabecalho()

lista_de_livros = [] # Essa lista guardará todos os livros cadastrados no sistema.

def cadastrar(titulo, autor, publicacao, codigo_isbn):
    # Cria o dicionário do livro cadastrado com as informações fornecidas.
    novo_livro = {"titulo": titulo.title(), "autor": autor.title(), "publicacao": publicacao, "isbn": codigo_isbn, "status": "disponível"}
    # O .title() deixa as primeiras letras maiúsculas, para padronizar a escrita e deixar mais organizado.
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
def excluir_cadastro():
    pass

def input_seguro(mensagem):
    resposta = input(mensagem).strip() # Retira os espaços vazios do que o usuário digitou, com o .strip().
    if resposta == "0": # Verifica se o usuário digitou 0 para voltar ao menu principal.
        raise Exception("CANCELADO") # Esse "cancelado" é apenas para indicar que o usuário cancelou a operação e não que um erro aconteceu.
    return resposta

while True: # Mantém o menu principal rodando continuamente até o usuário escolher a opção 7 para sair.
    print("=" * 40)
    print(" Sistema de Gerenciamento de Biblioteca")
    print("=" * 40)
    print("● 1. Cadastrar livro")
    print("● 2. Registrar empréstimo")
    print("● 3. Registrar devolução")
    print("● 4. Listar livros")
    print("● 5. Ordenar a listagem")
    print("● 6. Buscar livro")
    print("● 7. Sair do programa")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1": # Se o usuário digitar 1, entrará no bloco de cadastro de livro, mas ele pode sair quando quiser digitando 0.
        d.limpa()
        print("\n==== Cadastro de livro ====")
        print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

        try: # O programa vai tentar rodar este bloco inteiro.

            # Parte do título:
            while True:
                titulo = input_seguro("\nDigite o título do livro: ")
                if titulo == "":
                    print("\nO título não pode ficar em branco. Tente novamente.")
                else:
                    break # Para todos os "while True" os loops continuarão até que o usuário digite um valor válido para cada.

            # Parte do autor:
            while True:
                autor = input_seguro("\nDigite o autor: ")
                if autor == "": # Verifica se o usuário não digitou nada no input, se for verdade, pede para digitar novamente.
                    print("\nO autor não pode ficar em branco. Tente novamente.")
                else:
                    break

            # Parte do ano de publicação:
            while True:
                publicacao = input_seguro("\nDigite o ano de publicação: ")
                if publicacao == "":
                    print("\nO ano não pode ficar em branco. Tente novamente.\n") 
                elif publicacao.isdigit() and 1000 <= int(publicacao) <= 2026: # Verifica se a data digitada possui apenas números e está entre 1000 e 2026.
                    break
                else:
                    print("\nO ano digitado é inválido (muito grande ou muito pequeno). Tente novamente.")

            # Parte do código ISBN:
            while True:
                codigo_isbn = input_seguro("\nDigite o Código ISBN do livro: ")
                if codigo_isbn == "":
                    print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                    continue

                # Usa o .replace() para remover os traços e espaços, deixando só os números.
                codigo_isbn_limpo = codigo_isbn.replace(" ", "").replace("-", "")

                # 1º Teste: Verifica se o código digitado tem exatamente 13 números.
                if not (len(codigo_isbn_limpo) == 13 and codigo_isbn_limpo.isdigit()):
                    print("\nO código ISBN digitado é inválido (deve conter 13 números). Tente novamente.")
                    continue

                # 2º Teste: Verifica se o código ISBN já existe na lista de livros cadastrados.
                ja_cadastrado = False
                for livro in lista_de_livros:
                    if livro["isbn"] == codigo_isbn_limpo:
                        ja_cadastrado = True
                        break # Se já tiver um código igual, o programa pede para digitar outro código ISBN.
                if ja_cadastrado == True:
                    print("\nEste código ISBN já está cadastrado em outro livro na biblioteca. Tente novamente.")
                else:
                    codigo_isbn = codigo_isbn_limpo # Se não existir outro código igual e ele passar nos testes, ele é salvo.
                    break

            # Se o usuário não digitar 0 para voltar ao menu principal, o cadastro é finalizado.
            novo_livro = cadastrar(titulo, autor, publicacao, codigo_isbn) # Chama a função cadastrar() para criar o dicionário do livro com as informações fornecidas no input.
            lista_de_livros.append(novo_livro) # Adiciona o dicionário do livro na lista de livros cadastrados.
            print("\nLivro cadastrado com sucesso!")

        # Se ele digitar 0, o programa vai pular para esse bloco de exceção e mostrar a mensagem de cancelamento.
        except Exception: 
            d.limpa()
            print("\nCadastro cancelado. Voltando ao menu principal...")

    elif opcao == "2":
        emprestimo()
    elif opcao == "3":
        devolucao()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        ordenar()
    elif opcao == "6":
        buscar()
    elif opcao == "7":
        print("\nEncerrando o programa...")
        break
    else:
        print("\nOpção inválida, tente novamente.")