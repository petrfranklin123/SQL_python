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
        alter_table_query = """
        ALTER TABLE movies
        MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        show_table_query = "DESCRIBE movies"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            # Получить строки из последнего выполненного запроса
            result = cursor.fetchall()
            print("Схема таблицы movie после внесения изменений:")
            for row in result:
                print(row)
except Error as e:
    print(e)   







