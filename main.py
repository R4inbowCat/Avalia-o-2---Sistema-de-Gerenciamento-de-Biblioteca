import csv # Importa a biblioteca do csv para salvar os livros cadastrados na memória.
import definicoes as d # Importa as funções de limpar a tela e o cabeçalho que estão em outro arquivo.
d.limpa()
d.cabecalho()

arquivo_csv = "livros.csv" # Define o nome do arquivo CSV que será usado para salvar os livros cadastrados.
cabecalho_planilha = ["titulo", "autor", "publicacao", "isbn", "status"] # Define as categorias que serão usadas no cabeçalho do arquivo CSV.

def ler_arquivo_csv():
    lista = [] # Cria uma lista vazia para armazenar os livros cadastrados.
    try: # Tenta abrir o arquivo CSV apenas para leitura (mode="r").
        with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";") # Transforma as linhas do arquivo CSV em dicionários do Python.
            for linha in leitor:
                lista.append(dict(linha)) # Pega cada livro lido e guarda na lista da memória.
    except FileNotFoundError:
        pass  # Se o arquivo não tiver sido criado ainda, apenas inicia a lista vazia.
    return lista

def atualizar_arquivo_csv(lista):
    # Abre o arquivo no modo de escrita (mode="w"), que apaga o antigo e prepara para reescrever.
    with open(arquivo_csv, mode="w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho_planilha, delimiter=";") # Cria o escritor que vai escrever os dicionários na planilha CSV.
        # 1º passo: Escreve o cabeçalho lá no topo da planilha.
        escritor.writeheader()
        # 2º passo: Adiciona todos os livros da lista atualizada de uma vez só.
        escritor.writerows(lista)

def cadastrar(lista_de_livros):
    d.limpa()
    print("==== Cadastro de livro ====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

    try: # O programa vai tentar rodar este bloco inteiro.
        while True:
            # Parte do título:
            titulo = input_seguro("\nDigite o título do livro: ")
            if titulo == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue

            # Parte do autor:
            autor = input_seguro("\nDigite o autor: ")
            if autor == "": # Verifica se o usuário não digitou nada no input, se for verdade, pede para digitar novamente.
                print("\nO autor não pode ficar em branco. Tente novamente.")
                continue

            # Parte do ano de publicação:
            publicacao = input_seguro("\nDigite o ano de publicação: ")
            if publicacao == "":
                print("\nO ano não pode ficar em branco. Tente novamente.\n") 
                continue
            # Inverte a lógica: verifica se a data digitada não é número ou se está fora do limite.
            if not publicacao.isdigit() or not 1000 <= int(publicacao) <= 2026:
                print("\nO ano digitado é inválido (muito grande ou muito pequeno). Tente novamente.")
                continue

            # Parte do código ISBN:
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
            isbn_ja_cadastrado = False
            for livro in lista_de_livros:
                if livro["isbn"] == codigo_isbn_limpo:
                    isbn_ja_cadastrado = True
                    break

            if isbn_ja_cadastrado == True:
                # Se já tiver um código igual, o programa pede para digitar outro código ISBN.
                print("\nEste código ISBN já está cadastrado em outro livro na biblioteca. Tente novamente.")
                continue

            """Se o usuário não digitar 0 para voltar ao menu principal, o dicionário do livro 
            cadastrado é criado com as informações fornecidas nos inputs."""

            novo_livro = {"titulo": titulo.title(), "autor": autor.title(), "publicacao": publicacao, "isbn": codigo_isbn_limpo, "status": "disponível"}
            # O .title() deixa as primeiras letras maiúsculas, para padronizar a escrita e deixar mais organizado.
            lista_de_livros.append(novo_livro) # Adiciona o dicionário do livro na lista de livros cadastrados.
            atualizar_arquivo_csv(lista_de_livros) # Salva a lista de livros cadastrados no arquivo CSV.
            d.limpa()
            print(f"\nLivro {novo_livro['titulo']} cadastrado com sucesso!")
            break # Sai do loop de cadastro e volta para o menu principal.

    except Exception: 
        d.limpa()
        print("\nCadastro cancelado. Voltando ao menu principal...")
        """Se ele digitar 0, o programa vai pular para esse bloco de exceção e mostrar a mensagem de 
        cancelamento (essa mesma lógica é aplicada em quase todas as outras funções)."""

def emprestimo(lista_de_livros):
    d.limpa()
    print("==== Empréstimo de livro ====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")
    
    try:
        while True:
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro que deseja emprestar: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue

            codigo_isbn_limpo = codigo_isbn.replace(" ", "").replace("-", "")
            livro_encontrado = False
            sucesso_emprestimo = False

            for livro in lista_de_livros: # Percorre toda a lista de livros cadastrados para encontrar o livro com o código ISBN digitado pelo usuário.
                if livro["isbn"] == codigo_isbn_limpo:
                    livro_encontrado = True
                    if livro["status"] == "disponível":
                        livro["status"] = "emprestado"
                        atualizar_arquivo_csv(lista_de_livros)
                        d.limpa()
                        print(f"\nEmpréstimo do livro {livro['titulo']} registrado com sucesso!")
                        sucesso_emprestimo = True
                        break # Acaba com o laço de repetição do for.
                    else:
                        print("\nEste livro está indisponível no momento. Tente outro Código ISBN.")
                        break # Também serve para acabar com o for, mas pede o código novamente.

            if not livro_encontrado:
                """Se o livro não for encontrado após o laço de repetição procurar pela lista inteira, 
                mostra a mensagem de erro e pede para digitar o código ISBN novamente."""
                print("\nO Código ISBN digitado é inválido ou não está cadastrado na biblioteca. Tente novamente.")

            if sucesso_emprestimo == True:
                break # Se o empréstimo for bem-sucedido, sai do loop e volta para o menu principal.
            
    except Exception: 
        d.limpa()
        print("\nEmpréstimo cancelado. Voltando ao menu principal...")

def devolucao(lista_de_livros):
    d.limpa()
    print("==== Devolução de livro ====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

    # Essa função opera com a mesma lógica da função de empréstimo.
    try:
        while True:
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro que deseja devolver: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue
    
            codigo_isbn_limpo = codigo_isbn.replace(" ", "").replace("-", "")
            livro_encontrado = False
            sucesso_devolucao = False

            """Percorre a lista de livros para encontrar o que tem o mesmo código que o usuário digitou, 
            e verifica se ele realmente está emprestado. Se estiver, muda o status para 'disponível' 
            e salva a lista atualizada no arquivo CSV.""" 
            for livro in lista_de_livros:
                if livro["isbn"] == codigo_isbn_limpo:
                    livro_encontrado = True
                    if livro["status"] == "emprestado":
                        livro["status"] = "disponível"
                        atualizar_arquivo_csv(lista_de_livros)
                        d.limpa()
                        print(f"\nDevolução do livro {livro['titulo']} registrada com sucesso!")
                        sucesso_devolucao = True
                        break # Acaba com o laço de repetição do for.
                    else:
                        print("\nEste livro não está emprestado no momento. Tente outro Código ISBN.")
                        break # Também serve para acabar com o for, mas pede o código novamente.

            if not livro_encontrado:
                """Se o livro não for encontrado após o laço de repetição procurar pela lista inteira, 
                exibe a mensagem de erro e pede para digitar o código novamente."""
                print("\nO Código ISBN digitado é inválido ou não está cadastrado na biblioteca. Tente novamente.")
    
            if sucesso_devolucao == True:
                break # Se a devolução for bem-sucedida, sai do loop e volta para o menu principal.
                
    except Exception: 
        d.limpa()
        print("\nDevolução cancelada. Voltando ao menu principal...")

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

# A lista de livros é carregada quando o programa é iniciado.
lista_de_livros = ler_arquivo_csv()

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

    if opcao == "1":
        """Se o usuário digitar 1, entrará no bloco de cadastro de livro, mas ele pode sair 
        quando quiser digitando 0 (essa lógica é aplicada em todas as outras opções)."""
        cadastrar(lista_de_livros)

    elif opcao == "2":
        # Cada opção chama sua função correspondente, usando a lista de livros cadastrados como argumento.
        emprestimo(lista_de_livros)

    elif opcao == "3":
        devolucao(lista_de_livros)

    elif opcao == "4":
        listar(lista_de_livros)

    elif opcao == "5":
        ordenar(lista_de_livros)

    elif opcao == "6":
        buscar(lista_de_livros)

    elif opcao == "7":
        print("\nEncerrando o programa...")
        break

    else:
        print("\nOpção inválida, tente novamente.")