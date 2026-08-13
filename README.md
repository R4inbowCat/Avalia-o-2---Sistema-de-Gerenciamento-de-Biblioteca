# Sistema de Gerenciamento de Biblioteca

Um programa desenvolvido em Python para gerenciar o funcionamento de uma biblioteca diretamente pelo terminal. O sistema permite cadastrar, emprestar, devolver e excluir livros, salvando todos os dados de forma persistente em um arquivo `.csv`. Assim, os dados continuam salvos mesmo depois de fechar o programa.

## Como usar o programa:
- É necessário ter o Python instalado no computador.
- Baixe o código clonando o repositório com o link: `https://github.com/R4inbowCat/Avalia-o-2---Sistema-de-Gerenciamento-de-Biblioteca.git` 
- Certifique-se de que o arquivo principal **main.py** e o arquivo **definicoes.py** (utilizado para limpar a tela e formatar o cabeçalho) estejam na mesma pasta.
- **Nota para testes:** O arquivo **livros.csv** já vem com alguns livros previamente cadastrados. Isso facilita o teste imediato de todas as funcionalidades (como ordenação, busca, empréstimos e devoluções) sem a necessidade de cadastrar vários livros manualmente.
- Abra o terminal, execute o arquivo principal e siga atentamente as opções apresentadas no menu.
- Caso o arquivo **livros.csv** seja apagado, o sistema criará um novo arquivo limpo automaticamente.
- Para cancelar qualquer ação em andamento, basta digitar **0**. O sistema interrompe a operação e retorna ao menu principal.

## Principais funcionalidades:
- **Cadastrar livro:** Solicita o título, autor, ano de publicação e o código ISBN do livro desejado. O sistema impede cadastros em branco e exige que o ISBN possua exatamente 13 números.
- **Registrar empréstimo e devolução:** Altera o status do livro no sistema. O programa possui validações que impedem o empréstimo de um livro já emprestado ou a devolução de um livro que já consta como disponível.
- **Listar e ordenar:** Exibe todos os livros em uma tabela formatada. É possível visualizar a lista em ordem de cadastro, ordem alfabética, por ano de publicação, por autoria ou aplicar filtros para exibir apenas os livros disponíveis ou emprestados.
- **Buscar livro:** Busca rápida por título ou por autor. O usuário pode digitar apenas uma parte do nome do livro ou do nome do autor (independentemente de letras maiúsculas ou minúsculas) e o sistema localiza a obra na biblioteca.
- **Excluir cadastro:** Remove um livro do sistema, porém bloqueia a exclusão caso o livro ainda conste como emprestado para alguém.

## Requisitos técnicos aplicados no código:
- **Menu com if/elif/else:** Utilizado no bloco principal do arquivo para direcionar a navegação do usuário de acordo com a opção escolhida por ele.
- **Estrutura de repetição (while e for):** O `for` foi utilizado para percorrer toda a lista de livros cadastrados nas buscas e alterações. Já o `while True` foi aplicado para manter o menu principal ativo e para criar loops de validação até o usuário inserir uma resposta válida nos inputs.
- **Funções próprias com parâmetros e retorno:** Foram criadas para modularizar o sistema. Por exemplo, a função `ordenar()` retorna a lista já modificada para a função `listar()` utilizar. A função `gerenciar_livro(acao)` recebe parâmetros de texto (string), e a `input_seguro(mensagem)` recebe o texto da pergunta feita ao usuário e retorna a resposta dele validada.
- **Listas e dicionários:** A biblioteca inteira funciona como uma lista principal, enquanto cada livro inserido nela é um dicionário contendo suas próprias chaves (título, autor, publicação, isbn, status).
- **Persistência de dados em arquivo:** Uso da biblioteca padrão `csv` para ler a lista de livros salvos ao iniciar o programa (`ler_arquivo_csv`) e salvar (`atualizar_arquivo_csv`) a cada nova alteração feita.
- **Apenas bibliotecas padrão:** O projeto foi todo construído com lógica nativa e a biblioteca padrão `csv`, sem instalação de pacotes externos via pip.
- **Tratamento de erros (try/except):** Implementado nas funções principais para evitar a "quebra" do programa. Foi criada uma exceção (`OperacaoCancelada`), que é utilizada dentro da função `input_seguro()` quando o usuário digita "0". Isso separa um cancelamento intencional do usuário de um erro real do programa, que apareceria "escondido" no terminal.
- **Tratamento de textos de entrada:** Uso das funções `.strip()` para remover espaços em branco acidentais, `.lower()` para padronizar os textos (deixá-los minúsculos) e operador `or` para permitir a busca por título ou autor de uma só vez.