from getpass import getpass
from mysql.connector import connect, Error
'''
Чтобы установитть соединение, используем connect()
эта функция принимает три мараметра user, password и host
и возвращает объект MySQLConnection

Все соединения с БД оборачиваются в try except , таким обазом лучше всего можно перехватить данные 

Чтобы закрыть сессию с БД мы используем with as, если не закрыть, то это приведет к ошибкам 
'''

try:
    with connect(
        host ="localhost",
        user = "root",
        password = "",
        #Дополнительным параметром бросаем название базы данных 
        database = "onlline_movie_rating"
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
        print(connection)
        #добавляем строку для записи основной таблицы
        create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        create_ratings_table_query = """
        CREATE TABLE ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        #можно вставлять балицы последовательно, но рекомендуется добавлять их сразу все
        #вставляем ее в БД
        #with connection.cursor() as cursor:
        #    cursor.execute(create_movies_table_query)
        #    connection.commit()
    #кидаем запросы в БД 
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            connection.commit()
#если не вышло подключиться, то выводим шибку 
except Error as e:
    print(e)   







