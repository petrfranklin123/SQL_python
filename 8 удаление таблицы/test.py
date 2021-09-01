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
        password = "root",
        #Дополнительным параметром бросаем название базы данных 
        database = "onlline_movie_rating"
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
        drop_table_query = "DROP TABLE ratings"
        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
        #после удаления убеждаемся в том, что таблицы действительно нет 
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            #отправляем строку на выполнение 
            cursor.execute(show_db_query)
            #Вывод каждой БД
            for db in cursor:
                print(db)
                '''
        #чтобы у нас ничего не сломалоь, восстановим таблицу и убедимся в ее наличии
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
        #вставляем ее в БД
        with connection.cursor() as cursor:
            cursor.execute(create_ratings_table_query)
            connection.commit()
        #просматриваем возвращенную таблицу     
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            #отправляем строку на выполнение 
            cursor.execute(show_db_query)
            #Вывод каждой БД
            for db in cursor:
                print(db)'''
except Error as e:
    print(e)   


#вставка удаленной таблицы происходит через новую инициализацию, иначе не понимает 
try:
    with connect(
        host ="localhost",
        user = "root",
        password = "root",
        #Дополнительным параметром бросаем название базы данных 
        database = "onlline_movie_rating"
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
        #чтобы у нас ничего не сломалоь, восстановим таблицу и убедимся в ее наличии
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
        #вставляем ее в БД
        with connection.cursor() as cursor:
            cursor.execute(create_ratings_table_query)
            connection.commit()
        #просматриваем возвращенную таблицу     
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            #отправляем строку на выполнение 
            cursor.execute(show_db_query)
            #Вывод каждой БД
            for db in cursor:
                print(db)
except Error as e:
    print(e)   




