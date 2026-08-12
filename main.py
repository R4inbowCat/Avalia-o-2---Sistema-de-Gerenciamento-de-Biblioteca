import csv # Importa a biblioteca do csv para salvar os livros cadastrados na memória.
import definicoes as d # Importa as funções de limpar a tela e o cabeçalho que estão em outro arquivo.
d.limpa()
d.cabecalho()

arquivo_csv = "livros.csv" # Define o nome do arquivo CSV que será usado para salvar os livros cadastrados.
cabecalho_planilha = ["titulo", "autor", "publicacao", "isbn", "status"]
# Define as categorias que serão usadas no cabeçalho do arquivo CSV.

# FUNÇÕES DO PROGRAMA ---------------------------------------------------------------------------------------------------------

def ler_arquivo_csv():
    lista = [] # Cria uma lista vazia para armazenar os livros cadastrados.
    try: # Tenta abrir o arquivo CSV apenas para leitura (mode="r").
        with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo) # Transforma as linhas do arquivo CSV em dicionários do Python.
            for linha in leitor:
                lista.append(dict(linha)) # Pega cada livro lido e guarda na lista da memória.
    except FileNotFoundError:
        pass  # Se o arquivo não tiver sido criado ainda, apenas inicia a lista vazia.
    return lista

def atualizar_arquivo_csv(lista):
    # Abre o arquivo no modo de escrita (mode="w"), que apaga o antigo e prepara para reescrever.
    with open(arquivo_csv, mode="w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho_planilha)
        # Cria o escritor que vai escrever os dicionários na planilha CSV.
        
        # 1º passo: Escreve o cabeçalho lá no topo da planilha.
        escritor.writeheader()
        # 2º passo: Adiciona todos os livros da lista atualizada de uma vez só.
        escritor.writerows(lista)

def input_seguro(mensagem):
    # Essa função input_seguro() serve para verificar se o usuário digitou 0 para sair do menu principal.
    # O .strip() retira os espaços vazios do que o usuário digitou.
    resposta = input(mensagem).strip()
    if resposta == "0":
        # O "cancelado" é apenas para indicar que o usuário cancelou a operação e não que um erro aconteceu.
        raise Exception("CANCELADO")
    return resposta

def cadastrar():
    # A lista de livros é carregada quando o programa é iniciado.
    lista_de_livros = ler_arquivo_csv()
    d.limpa()
    print("===== Cadastro de livro =====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

    try: # O programa vai tentar rodar este bloco inteiro.
        # Parte do título:
        while True:
            titulo = input_seguro("\nDigite o título do livro: ")
            if titulo == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue
            break # Se o usuário digitou algo válido, sai do loop e passa para a próxima pergunta.

        # Parte do autor:
        while True:
            autor = input_seguro("\nDigite o autor: ")
            if autor == "":
            # Verifica se o usuário não digitou nada no input, se for verdade, pede para digitar novamente.
                print("\nO autor não pode ficar em branco. Tente novamente.")
                continue
            break

        # Parte do ano de publicação:
        while True:
            publicacao = input_seguro("\nDigite o ano de publicação: ")
            if publicacao == "":
                print("\nO ano não pode ficar em branco. Tente novamente.\n") 
                continue
            # Inverte a lógica: verifica se a data digitada não é número ou se está fora do limite.
            if not publicacao.isdigit() or not 1000 <= int(publicacao) <= 2026:
                print("\nO ano digitado é inválido (muito grande ou muito pequeno). Tente novamente.")
                continue
            break

        # Parte do código ISBN:
        while True:
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue

            # Verifica se o código digitado tem exatamente 13 números.
            if not (len(codigo_isbn) == 13 and codigo_isbn.isdigit()):
                print("\nO código ISBN digitado é inválido (deve conter 13 números). Tente novamente.")
                continue
            break

        # Se o usuário não digitar 0 para voltar ao menu principal, o dicionário do livro 
        # cadastrado é criado com as informações fornecidas nos inputs.

        novo_livro = {"titulo": titulo, "autor": autor, "publicacao": publicacao, "isbn": codigo_isbn, "status": "disponivel"}
        lista_de_livros.append(novo_livro) # Adiciona o dicionário do livro na lista de livros cadastrados.
        atualizar_arquivo_csv(lista_de_livros) # Salva a lista de livros cadastrados no arquivo CSV.
        d.limpa()
        print(f"\n● Livro {novo_livro['titulo']} cadastrado com sucesso!")

    except Exception: 
        d.limpa()
        print("\nCadastro cancelado. Voltando ao menu principal...")
        # Se ele digitar 0, o programa vai pular para esse bloco de exceção e mostrar a mensagem de 
        # cancelamento (essa mesma lógica é aplicada em quase todas as outras funções).

def emprestimo():
    lista_de_livros = ler_arquivo_csv()
    d.limpa()
    print("===== Empréstimo de livro =====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")
    
    try:
        while True:
            titulo = input_seguro("\nDigite o título do livro que deseja emprestar: ")
            if titulo == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro que deseja emprestar: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue

            livro_encontrado = False
            sucesso_emprestimo = False

            # Percorre toda a lista de livros cadastrados para encontrar o livro com o código e título digitados pelo usuário.
            for livro in lista_de_livros:
                if livro["isbn"] == codigo_isbn and livro["titulo"] == titulo:
                    livro_encontrado = True
                    if livro["status"] == "disponivel":
                        livro["status"] = "emprestado"
                        atualizar_arquivo_csv(lista_de_livros)
                        d.limpa()
                        print(f"\n● Empréstimo do livro {livro['titulo']} registrado com sucesso!")
                        sucesso_emprestimo = True
                        break # Acaba com o laço de repetição do for.
                    else:
                        print("\nEste livro está indisponível no momento. Tente outro livro.")
                        break # Também serve para acabar com o for, mas pede o código novamente.

            if not livro_encontrado == True:
                # Se o livro não for encontrado após o laço de repetição procurar pela lista inteira, 
                # mostra a mensagem de erro e pede para o usuário digitar novamente.
                print("\nO título ou o código digitado é inválido ou não está cadastrado na biblioteca. Tente novamente.")

            if sucesso_emprestimo == True:
                break # Se o empréstimo for bem-sucedido, sai do loop e volta para o menu principal.
            
    except Exception: 
        d.limpa()
        print("\nEmpréstimo cancelado. Voltando ao menu principal...")

def devolucao():
    lista_de_livros = ler_arquivo_csv()
    d.limpa()
    print("===== Devolução de livro =====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

    # Essa função opera com a mesma lógica da função de empréstimo.
    try:
        while True:
            titulo = input_seguro("\nDigite o título do livro que deseja devolver: ")
            if titulo == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro que deseja devolver: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue
    
            livro_encontrado = False
            sucesso_devolucao = False

            # Percorre a lista de livros para encontrar o que tem o mesmo código que o usuário digitou, 
            # e verifica se ele realmente está emprestado. Se estiver, muda o status para 'disponível' 
            # e salva a lista atualizada no arquivo CSV. 
            for livro in lista_de_livros:
                if livro["isbn"] == codigo_isbn and livro["titulo"] == titulo:
                    livro_encontrado = True
                    if livro["status"] == "emprestado":
                        livro["status"] = "disponivel"
                        atualizar_arquivo_csv(lista_de_livros)
                        d.limpa()
                        print(f"\n● Devolução do livro {livro['titulo']} registrada com sucesso!")
                        sucesso_devolucao = True
                        break # Acaba com o laço de repetição do for.
                    else:
                        print("\nEste livro não está emprestado no momento. Tente outro livro.")
                        break # Também serve para acabar com o for, mas pede o código novamente.

            if not livro_encontrado:
                # Se o livro não for encontrado após o laço de repetição procurar pela lista inteira, 
                # exibe a mensagem de erro e pede para digitar o código novamente.
                print("\nO título ou o código digitado é inválido ou não está cadastrado na biblioteca. Tente novamente.")
    
            if sucesso_devolucao == True:
                break # Se a devolução for bem-sucedida, sai do loop e volta para o menu principal.
                
    except Exception: 
        d.limpa()
        print("\nDevolução cancelada. Voltando ao menu principal...")

def listar():
    lista_de_livros = ler_arquivo_csv()
    # Chama a função ordenar e guarda a nova lista ordenada.
    lista_ordenada = ordenar()
    d.limpa()
    print("===== Listagem de livros =====\n")
    
    try:
        while True:
            # Se a biblioteca não possuir nenhum livro cadastrado, a listagem não ocorre e retorna ao menu.
            if len(lista_de_livros) == 0:
                print("\nNenhum livro foi cadastrado ainda. Tente novamente mais tarde.")
                input_seguro("\nDigite '0' para voltar ao menu principal: ")

            elif lista_ordenada is None:
                return # Se o usuário cancelar a ordenação, a função listar() também é cancelada.

            elif len(lista_ordenada) == 0:
                print("\nNão há livros com o status escolhido na biblioteca. Tente novamente.")
                input_seguro("\nDigite '0' para voltar ao menu principal: ")

            else: 
                # Exibe o cabeçalho da tabela com os títulos das colunas, e uma linha de separação.
                print(f"{'TÍTULO':<25} | {'AUTOR(A)':<20} | ANO   | ISBN            | STATUS")
                print("-" * 93)

                # O for vai percorrer a lista de livros e exibir cada livro em uma linha da tabela.
                for livro in lista_ordenada:
                    titulo = livro['titulo']
                    autor = livro['autor']

                    # Se o título for maior que 25 letras, o sistema "corta" para a tabela não ficar 
                    # desorganizada, e adiciona "..." no final para indicar que o título foi cortado.
                    if len(titulo) > 25:
                        titulo = titulo[:22] + "..."
                        
                    # Faz a mesma coisa com o autor se for maior que 20 letras.
                    if len(autor) > 20:
                        autor = autor[:17] + "..."
                    
                    # Exibe os livros da biblioteca usando a mesma formatação do cabeçalho (os :<25 ou 
                    # :<20 servem para garantir que o espaço onde o texto está fique do tamanho certo).
                    print(f"{titulo:<25} | {autor:<20} | {livro['publicacao']:<5} | {livro['isbn']:<15} | {livro['status']}")
                print("-" * 93)

                input_seguro("\nDigite '0' quando desejar voltar para o menu principal: ")
                
    except Exception: 
        d.limpa()
        print("\nListagem cancelada. Voltando ao menu principal...")

# FUNÇÕES AUXILIARES PARA A DE ORDENAÇÃO ---------------------------------------------------------------------------------------------------------

def listar_por_titulo(livro):
    return livro["titulo"]

def listar_por_ano(livro):
    return int(livro["publicacao"]) # O int converte em número para ordenar corretamente os anos de publicação.

def listar_por_status(status_desejado):
    lista_de_livros = ler_arquivo_csv()
    lista_ordenada = []
    # O for e o if selecionam todos os livros da biblioteca de acordo com o status (disponível ou emprestado).
    for livro in lista_de_livros:
        if livro["status"] == status_desejado:
            # Adiciona o livro na lista ordenada se o status for igual ao escolhido pelo usuário.
            lista_ordenada.append(livro)
    return lista_ordenada

def ordenar():
    lista_de_livros = ler_arquivo_csv()
    
    try:
        while True:
            d.limpa()
            print("===== Ordenação de livros =====")
            print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

            print("\nComo você deseja visualizar a lista de livros?")
            print("● 1 - Todos os livros (ordem de cadastro)")
            print("● 2 - Ordem alfabética (por título)")
            print("● 3 - Ordem de ano de publicação")
            print("● 4 - Apenas livros disponíveis")
            print("● 5 - Apenas livros emprestados")
            opcao_ordem = input_seguro("\nEscolha a opção desejada: ")

            # Ordenação padrão: apenas retorna a lista inteira de livros sem mexer em nada.
            if opcao_ordem == "1":
                return lista_de_livros

            # Ordenação alfabética: o sorted usa a função listar_por_titulo() como chave de organização.
            elif opcao_ordem == "2":
                return sorted(lista_de_livros, key=listar_por_titulo) 

            # Ordenação por ano de publicação: o sorted usa a função listar_por_ano() como chave para organizar.
            elif opcao_ordem == "3":
                return sorted(lista_de_livros, key=listar_por_ano) 

            # Ordenação por status (disponível ou emprestado): cria uma nova lista apenas com os livros que têm o status desejado.
            elif opcao_ordem == "4":
                return listar_por_status("disponivel")

            elif opcao_ordem == "5":
                return listar_por_status("emprestado")

            else:
                print("\nOpção inválida. Tente novamente.")

    except Exception: 
        d.limpa()
        print("\nOrdenação cancelada. Voltando ao menu principal...")
        return None

def buscar():
    lista_de_livros = ler_arquivo_csv()

    try: 
        while True:
            d.limpa()
            print("===== Busca de livros =====")
            print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")

            # O .strip() tira os espaços das bordas e o .lower() deixa tudo em minúsculo para facilitar a busca.
            titulo_busca = input_seguro("\nDigite o título do livro que deseja buscar: ").strip().lower()
            if titulo_busca == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue
            # Cria uma lista temporária para guardar todos os livros que forem selecionados na busca.
            livros_encontrados = []
            # Percorre toda a "biblioteca" comparando o texto digitado com os títulos cadastrados.
            for livro in lista_de_livros:
                titulo_minusculo = livro["titulo"].lower()
                # O in permite achar o livro mesmo se o usuário digitar só uma parte do nome.
                if titulo_busca in titulo_minusculo:
                    livros_encontrados.append(livro)

            # Se a lista temporária continuar vazia, significa que a busca não encontrou nada.
            # Se não, cria a tabela formatada com os resultados encontrados.
            if len(livros_encontrados) == 0:
                print("\nNenhum livro com o título digitado foi encontrado. Tente novamente.")
            else:
                d.limpa()
                print(f"===== Resultados da busca =====\n")
                print(f"● {len(livros_encontrados)} livro(s) encontrado(s)\n")
                print(f"{'TÍTULO':<25} | {'AUTOR(A)':<20} | ANO   | ISBN            | STATUS")
                print("-" * 93)

                for livro in livros_encontrados:
                    titulo = livro['titulo']
                    autor = livro['autor']
                    if len(titulo) > 25:
                        titulo = titulo[:22] + "..."
                    if len(autor) > 20:
                        autor = autor[:17] + "..."
                    print(f"{titulo:<25} | {autor:<20} | {livro['publicacao']:<5} | {livro['isbn']:<15} | {livro['status']}")
                print("-" * 93)
            while True:
                escolha = input_seguro("\nDigite '0' para voltar ao menu ou aperte 'Enter' para fazer uma nova busca: ")
                if escolha == '':
                    break # Quebra apenas o while True, fazendo o programa voltar para o início da busca.
                else:
                    print("\nValor digitado inválido. Tente novamente.")

    except Exception: 
        d.limpa()
        print("\nBusca cancelada. Voltando ao menu principal...")

def excluir_cadastro():
    lista_de_livros = ler_arquivo_csv()
    d.limpa()
    print("===== Exclusão de livro =====")
    print("\n(Digite '0' em qualquer pergunta para cancelar e voltar ao menu principal.)")
    
    try:
        while True:
            titulo = input_seguro("\nDigite o título do livro que deseja excluir: ")
            if titulo == "":
                print("\nO título não pode ficar em branco. Tente novamente.")
                continue
            codigo_isbn = input_seguro("\nDigite o Código ISBN do livro que deseja excluir: ")
            if codigo_isbn == "":
                print("\nO Código ISBN não pode ficar em branco. Tente novamente.")
                continue
        
            livro_encontrado = False
            sucesso_exclusao = False
    
            # Esse laço de repetição percorrerá toda a lista de livros para encontrar um que tenha o 
            # mesmo código que o usuário digitou, e verificará se ele está emprestado. Se estiver, não será 
            # possível excluí-lo. Se não estiver, exclui o livro e salva a lista atualizada no arquivo CSV.
            for livro in lista_de_livros:
                if livro["isbn"] == codigo_isbn and livro["titulo"] == titulo:
                    livro_encontrado = True
                    if livro["status"] == "emprestado":
                        print("\nEste livro está emprestado no momento. Não é possível excluí-lo. Tente outro livro.")
                        break # Encerra o "for" e pede para o usuário digitar novamente.
                    else:
                        lista_de_livros.remove(livro) # Remove o livro da lista de livros cadastrados.
                        atualizar_arquivo_csv(lista_de_livros)
                        d.limpa()
                        print(f"\n● Exclusão do livro {livro['titulo']} registrada com sucesso!")
                        sucesso_exclusao = True
                        break # Acaba com o laço de repetição do for.
    
            if not livro_encontrado:
                # Se o livro não for encontrado, mostra um aviso de erro e pede para digitar o código de novo.
                print("\nO título ou o código digitado é inválido ou não está cadastrado na biblioteca. Tente novamente.")
        
            if sucesso_exclusao == True:
                break # Se a exclusão for bem-sucedida, sai do loop e volta para o menu principal.
                    
    except Exception: 
        d.limpa()
        print("\nExclusão cancelada. Voltando ao menu principal...")

# MENU PRINCIPAL DO PROGRAMA ---------------------------------------------------------------------------------------------------------

while True: # Mantém o menu rodando continuamente até o usuário escolher a opção 7 para sair.
    print("⁓" * 40)
    print(" Sistema de Gerenciamento de Biblioteca")
    print("⁓" * 40)
    print("● 1. Cadastrar livro")
    print("● 2. Registrar empréstimo")
    print("● 3. Registrar devolução")
    print("● 4. Ordenar e listar livros")
    print("● 5. Buscar livro")
    print("● 6. Excluir cadastro")
    print("● 7. Sair do programa")
    opcao = input("\nEscolha uma opção: ")

    # Cada função é chamada de acordo com a opção escolhida pelo usuário, e ele pode voltar ao 
    # menu quando quiser, digitando 0 em qualquer pergunta.
    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        emprestimo()

    elif opcao == "3":
        devolucao()

    elif opcao == "4":
        listar()

    elif opcao == "5":
        buscar()

    elif opcao =="6":
        excluir_cadastro()

    elif opcao == "7":
        print("\nEncerrando o programa... Até logo!")
        break

    else:
        print("\nOpção inválida, tente novamente.")