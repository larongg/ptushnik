import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()


def get_name(id):
    global connection, cursor

    cursor.execute("SELECT name FROM users WHERE id = ?", (id, ))
    return cursor.fetchone()[0]


def registration(name, password, mail):
    global connection, cursor

    user = (name, password, mail)
    cursor.execute("INSERT INTO users (name, password, mail) VALUES(?, ?, ?);", user)
    connection.commit()


def create_post(title, text, date, author):
    global connection, cursor

    post = (title, text, 0, date, author)
    cursor.execute("INSERT INTO posts (title, text, rating, date, author) VALUES(?, ?, ?, ?, ?);", post)
    connection.commit()


def login(name, password):
    global connection, cursor

    cursor.execute("SELECT name, password FROM users WHERE name = ?", (name, ))
    real_name, real_password = cursor.fetchone()
    if name == real_name and password == real_password:
        return True
    else:
        return False


def delete_post(id):
    global connection, cursor

    cursor.execute("DELETE FROM posts WHERE id = ?", (id, ))
    connection.commit()


# def change_post(id, title, text)
def show_post(query, req=None):
    global connection, cursor

    if type(query) is int and req is None:
        # Ищем все посты по id автора
        cursor.execute("SELECT * FROM posts WHERE author = ?", (query, ))
        results = cursor.fetchall()
        return results

    elif type(query) is str and req in ("DESC", "ASC"):
        response = f"SELECT * FROM posts ORDER BY {query} {req}"
        cursor.execute(response)
        results = cursor.fetchall()
        return results
    else:
        raise TypeError


def main():
    # registration("Dimsdfa", "dssfdsf3234", 'sdfs3@esdfml.com')
    # create_post("Title2", "Text2", "03.11.2022", 3)
    # print(login("Lev", '111'))
    # delete_post(4)
    # print(show_post(1))
    # print(show_post("author", "ASC"))
    pass


if __name__ == "__main__":
    main()
