
from datetime import datetime, timedelta
from faker import Faker
import sqlite3
import random
import os
fake = Faker()

def create_db_file(sql_file, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    with open(sql_file, 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)

    conn.commit()
    conn.close()

def insert_data_sql(database):
    # DB Connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Insert country
    country = [(1, 'Brasil'), (2, 'Estados Unidos'), (3, 'Reino Unido')]
    cursor.executemany('INSERT OR IGNORE INTO País (Código_do_País, Nome_do_País) VALUES (?, ?)', country)
    # Insert city
    city = [(1, 'São Paulo'), (2, 'Nova York'), (3, 'Londres')]
    cursor.executemany('INSERT OR IGNORE INTO Cidade (Código_da_Cidade, Nome_da_Cidade) VALUES (?, ?)', city)
    # Insert literary_gender
    literary_gender = [(1, 'Ficção Científica'), (2, 'Fantasia'), (3, 'Romance')]
    cursor.executemany('INSERT OR IGNORE INTO Tipo_de_Gênero_Literário (Código_do_Gênero_Literário, Nome_do_Gênero_Literário) VALUES (?, ?)', literary_gender)
    # Insert gender
    gender = [(1, 'Masculino'), (2, 'Feminino'), (3, 'Não binário')]
    cursor.executemany('INSERT OR IGNORE INTO Tipo_de_Gênero (Código_do_Gênero, Nome_do_Gênero) VALUES (?, ?)', gender)
    # Insert education level
    education_level = [(1, 'Ensino Médio'), (2, 'Graduação'), (3, 'Pós-graduação')]
    cursor.executemany('INSERT OR IGNORE INTO Tipo_de_Escolaridade (Código_da_escolaridade, Descrição_da_escolaridade) VALUES (?, ?)', education_level)
    # Insert matrial status
    marital_status = [(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Divorciado(a)')]
    cursor.executemany('INSERT OR IGNORE INTO Tipo_de_Estado_Cívil (Código_do_Estado_Cívil, Descrição_do_Estado_Cívil) VALUES (?, ?)', marital_status)

    # Generate and Insert fictional book data
    book = []
    for _ in range(50):
        title = fake.sentence()
        year = fake.year()
        edtion = random.randint(1, 10)
        isbn = fake.isbn13()
        publisher = random.randint(1, 3)  
        literary_gender = random.randint(1, 3) 
        author = random.randint(1, 50)
        book.append((title, year, edtion, isbn, publisher, literary_gender, author))

    cursor.executemany('''INSERT OR IGNORE INTO Livro (Texto_do_Título, Ano_de_publicação, Número_da_Edição, Código_ISBN, idEditora, idGênero_Literário, idAutor)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', book)
    
    # Generate and Insert fictional author data
    author = []
    for i in range(1, 51):
        author_name = fake.name()
        country = random.randint(1, 3) 
        author.append((i, author_name, country))

    cursor.executemany('''INSERT OR IGNORE INTO Autor (Código_do_Autor, Nome_Completo_do_Autor, idPaís) VALUES (?, ?, ?)''', author)

    # Generate and Insert fictional publisher data
    publisher = []
    for i in range(1, 4):  
        id_publisher = fake.random_int(min=1000, max=9999)
        name_publisher = fake.company()
        country = random.randint(1, 3)
        city = random.randint(1, 3) 
        publisher.append((id_publisher, name_publisher, country, city))

    cursor.executemany('''INSERT OR IGNORE INTO Editora (Código_da_Editora, Nome_da_Editora, idPaís, idCidade) VALUES (?, ?, ?, ?)''', publisher)

    # Generate and Insert fictional user data
    user = []
    for _ in range(50):
        cpf = fake.random_int(min=10000000000, max=99999999999)  # CPF is the Person ID in Brazil
        user_name = fake.name()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
        gender = random.randint(1, 3)  
        email_adress = fake.email()
        adress = fake.address()
        education_level = random.randint(1, 3) 
        matrial_status = random.randint(1, 3)
        telephone = fake.phone_number()
        active_user = random.randint(0, 1)
        user.append((cpf, user_name, birth_date, gender, email_adress, adress, education_level, matrial_status, telephone, active_user))
    
    cursor.executemany('''INSERT OR IGNORE INTO Usuário (CPF, Nome_do_Usuário, Data_de_Nascimento, idGênero, Texto_do_Endereço_de_Email, Endereço, idTipo_de_Escolaridade, idTipo_de_Estado_Cívil, Numero_de_telefone, Indicador_de_Usuário_Ativo)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', user)
    
    # Generate and Insert fictional loan data
    loan = []
    for _ in range(100):
        id_user = fake.random_int(min=10000000000, max=99999999999)  # CPF é um número de 11 dígitos
        id_copy_book = random.randint(1, 50)  
        id_book = random.randint(1, 50)  
        loan_timestamp = fake.date_time_between(start_date="-1y", end_date="now")
        return_date = loan_timestamp + timedelta(days=random.randint(7, 30))
        loan.append((id_user, id_copy_book, id_book, loan_timestamp, return_date))

    cursor.executemany('''INSERT OR IGNORE INTO Emprestimo (idUsuário, idExemplar, idLivro, Timestamp_do_Momento_do_Emprestimo, Data_de_Devolução_do_Exemplar)
                        VALUES (?, ?, ?, ?, ?)''', loan)

    # Commit and close db connection
    conn.commit()
    conn.close()

# Função para consultar a tabelas do BD e chekar inserção
def query_table(database):
    # db_connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # query table
    cursor.execute("SELECT * FROM Autor")
    #cursor.execute("SELECT * FROM Editora")
    #cursor.execute("SELECT * FROM País")
    #cursor.execute("SELECT * FROM city")
    #cursor.execute("SELECT * FROM Tipo_de_Gênero_Literário")
    #cursor.execute("SELECT * FROM Tipo_de_Gênero")
    #cursor.execute("SELECT * FROM Tipo_de_Escolariade")
    #cursor.execute("SELECT * FROM Tipo_de_Estado_Cívil")

    tabelaSelecionada = cursor.fetchall()

    # show results
    #print("book:")
    for tabela in tabelaSelecionada:
        print(tabela)

    # close connection
    conn.close()

def main():
    # Select db name
    abs_path = os.path.dirname(os.path.abspath(__file__))
    sql_file = os.path.join(abs_path, "SQLgenerateFromModelagem.sql")
    database = "LibraryBYU.db"

    # Executa o arquivo SQL
    create_db_file(sql_file, database)

    # Insert data Ficticios
    insert_data_sql(database)

    # Consulta a tabela Livro
    query_table(database)


if __name__ == "__main__":
    main()