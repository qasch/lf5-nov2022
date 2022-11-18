import sqlite3

# Verbindung zur Datenbank herstellen
connection = sqlite3.connect('gfn.db')

# Cursor erzeugen
cursor = connection.cursor()

def drop_table():
    sql_statement = """
        DROP TABLE IF EXISTS gfn;
    """
    cursor.execute(sql_statement)


def create_tables()
    sql_statement = """
        CREATE TABLE gfn (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            beschwerde TEXT,
            kurs TEXT,
            trainer TEXT,
            datum TEXT
            );
        """

    cursor.execute(sql_statement)


def insert_data():
    sql_statement = """
        INSERT INTO gfn (
            beschwerde,
            kurs,
            trainer,
            datum
            )
        VALUES 
            ("zu viel Stoff", "LF5", "Kai Schell", "2022-10-21 15:18:34"),
            ("LZK zu schwer", "LF5", "Kai Schell", "1666351018"),
            ("Gretl schnarcht viel zu laut", "LF20", "Kurt Haensel", "1666352345");
    """
    cursor.execute(sql_statement)


drop_table()
create_tables()
insert_data()

# Änderungen an DB übertragen
connection.commit()
# Verbindung schliessen
connection.close()
