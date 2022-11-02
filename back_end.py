import sqlite3


def login(login, password):
    '''login function'''
    pass


def registration(cursor, name, password):
    cursor.execute()


def main():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    registration(cursor, "Alex", "1234")


if __name__ == "__main__":
    main()
