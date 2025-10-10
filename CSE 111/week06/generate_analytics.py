import sqlite3
import pandas as pd

def qty_book_per_author(database):
    # db connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT aut.Código_do_Autor, aut.Nome_Completo_do_Autor,count(*) as qty_book_per_author FROM Livro liv left join Autor aut on liv.idAutor = aut.Código_do_Autor group by aut.Código_do_Autor, aut.Nome_Completo_do_Autor")

    tabelaSelecionada = cursor.fetchall()

    # get columns names
    columns = [description[0] for description in cursor.description]

    # create df
    df = pd.DataFrame(tabelaSelecionada, columns=columns)
    print(df)

    # close connection
    conn.close()

def user_by_letter(database):
    # db connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuário WHERE Nome_do_Usuário LIKE ?", ('T%',))

    tabelaSelecionada = cursor.fetchall()

    # get columns names
    columns = [description[0] for description in cursor.description]

    # Create dataframe
    df = pd.DataFrame(tabelaSelecionada, columns=columns)
    print(df)

    # close connection
    conn.close()

def suspended_users(database):
    # db connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuário WHERE Indicador_de_Usuário_Ativo = 0")

    tabelaSelecionada = cursor.fetchall()

    # get columns names
    columns = [description[0] for description in cursor.description]

    # Create df
    df = pd.DataFrame(tabelaSelecionada, columns=columns)
    print(df)

    # close connection
    conn.close()

def main():
    # db name
    database = "LibraryBYU.db"

    #analytics
    #qty_book_per_author(database)
    #user_by_letter(database)
    suspended_users(database)

if __name__ == "__main__":
    main()