import definicoes as d
d.limpa()
d.cabecalho()

def cadastrar():
    pass
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
        cadastrar()
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