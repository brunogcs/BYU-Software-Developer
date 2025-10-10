# Análise de Biblioteca

Este projeto passou pelas seguintes fases

### 1. Modelagem dos dados utilizando "brmodeloweb"
### 2. Gerar dados utilizando bibliotecas Python como Random e Faker
### 3. Estrutura de dados criada no sqlite
### 4. Dados carregados no BD criado
### 5. Criado algumas funções de interesse da biblioteca (Essas funções executam códigos simples em SQL)


## Exemplos de Funções

### 1. Quantidade de Livros por Autor

A função `qtd_livro_autor` retorna a quantidade de livros que cada autor possui. Ela faz uma consulta no banco de dados e cria um DataFrame com os resultados.

### 2. Usuários que Começam com a Letra "T"

A função `usuario_por_letra` busca os usuários cujos nomes começam com a letra "T". Ela também cria um DataFrame com os resultados.

### 3. Usuários Suspensos

A função `usuario_suspenso` retorna os usuários que estão suspensos por não devolverem livros alugados. Novamente, os resultados são armazenados em um DataFrame.
