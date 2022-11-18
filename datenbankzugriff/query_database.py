import sqlite3

connection = sqlite3.connect('gfn.db')
cursor = connection.cursor()


def get_all_data():
    sql_statement = """
        SELECT * FROM gfn;
    """

    return cursor.execute(sql_statement).fetchall()


def print_data():
    for row in get_all_data():
        print(row)


def print_all_beschwerden():
    for row in get_all_data():
        print("Beschwerde: " + row[1])


# print(type(get_all_data()))

# print_data()
print_all_beschwerden()
connection.close()