/*Por causa da plataforma que usei para modelar os nomes vieram com acento, não é uma boa pratica porém como não criei abreviatura fisicas deixai como está*/

CREATE TABLE IF NOT EXISTS  Livro (
    Texto_do_Título TEXT,
    Ano_de_publicação INTEGER,
    Número_da_Edição INTEGER PRIMARY KEY,
    Código_ISBN TEXT,
    idEditora INTEGER,
    idGênero_Literário INTEGER,
    idAutor INTEGER,
    FOREIGN KEY(idEditora) REFERENCES Editora(Código_da_Editora),
    FOREIGN KEY(idGênero_Literário) REFERENCES Tipo_de_Gênero_Literário(Código_do_Gênero_Literário),
    FOREIGN KEY(idAutor) REFERENCES Autor(Código_do_Autor)
);

CREATE TABLE IF NOT EXISTS  Editora (
    Código_da_Editora TEXT PRIMARY KEY,
    Nome_da_Editora TEXT,
    idPaís INTEGER,
    idCidade INTEGER,
    FOREIGN KEY(idPaís) REFERENCES País(Código_do_País),
    FOREIGN KEY(idCidade) REFERENCES Cidade(Código_da_Cidade)
);

CREATE TABLE IF NOT EXISTS  Autor (
    Código_do_Autor INTEGER PRIMARY KEY,
    Nome_Completo_do_Autor TEXT,
    idPaís INTEGER,
    FOREIGN KEY(idPaís) REFERENCES País(Código_do_País)
);

CREATE TABLE IF NOT EXISTS  País (
    Código_do_País INTEGER PRIMARY KEY,
    Nome_do_País TEXT
);

CREATE TABLE IF NOT EXISTS  Cidade (
    Código_da_Cidade INTEGER PRIMARY KEY,
    Nome_da_CIdade TEXT
);

CREATE TABLE IF NOT EXISTS Tipo_de_Gênero_Literário (
    Código_do_Gênero_Literário INTEGER PRIMARY KEY,
    Nome_do_Gênero_Literário TEXT
);

CREATE TABLE IF NOT EXISTS Exemplar (
    idLivro INTEGER PRIMARY KEY,
    Numero_Sequencial_do_Exemplar INTEGER,
    Data_de_aquisição DATE,
    Indicador_de_Exemplar_Ativo INTEGER,
    FOREIGN KEY(idLivro) REFERENCES Livro(Número_da_Edição)
);

CREATE TABLE IF NOT EXISTS Usuário (
    CPF INTEGER PRIMARY KEY,
    Nome_do_Usuário TEXT,
    Data_de_Nascimento DATE,
    idGênero INTEGER,
    Texto_do_Endereço_de_Email TEXT,
    Endereço TEXT,
    idTipo_de_Escolaridade INTEGER,
    idTipo_de_Estado_Cívil INTEGER,
    Numero_de_Telefone INTEGER,
    Indicador_de_Usuário_Ativo INTEGER,
    FOREIGN KEY(idGênero) REFERENCES Tipo_de_Gênero(Código_do_Gênero),
    FOREIGN KEY(idTipo_de_Escolaridade) REFERENCES Tipo_de_Escolaridade(Código_da_Escolaridade),
    FOREIGN KEY(idTipo_de_Estado_Cívil) REFERENCES Tipo_de_Estado_Cívil(Código_do_Estado_Cívil)
);

CREATE TABLE IF NOT EXISTS Tipo_de_Gênero (
    Código_do_Gênero INTEGER PRIMARY KEY,
    Nome_do_Gênero TEXT
);

CREATE TABLE IF NOT EXISTS Tipo_de_Escolaridade (
    Código_da_Escolaridade INTEGER PRIMARY KEY,
    Descrição_da_Escolaridade TEXT
);

CREATE TABLE IF NOT EXISTS Tipo_de_Estado_Cívil (
    Código_do_Estado_Cívil INTEGER PRIMARY KEY,
    Descrição_do_Estado_Cívil TEXT
);

CREATE TABLE IF NOT EXISTS Emprestimo (
    idUsuário INTEGER,
    idExemplar INTEGER,
    idLivro INTEGER,
    Timestamp_do_Momento_do_Emprestimo DATE,
    Data_de_Devolução_do_Exemplar DATE,
    PRIMARY KEY (idUsuário, idExemplar, idLivro, Timestamp_do_Momento_do_Emprestimo),
    FOREIGN KEY(idUsuário) REFERENCES Usuário(CPF),
    FOREIGN KEY(idExemplar) REFERENCES Exemplar(idLivro),
    FOREIGN KEY(idLivro) REFERENCES Livro(Número_da_Edição)
);