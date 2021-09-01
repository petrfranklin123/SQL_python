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
        '''
        Выбираем два столбца из таблицы muvies и сортирум в обратном порядке 
        при этом больше 300
        '''
        select_movies_query = """
        SELECT title, collection_in_mil
        FROM movies
        WHERE collection_in_mil > 300
        ORDER BY collection_in_mil DESC
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
        #----------------------------------------------------------------------        
        '''
        если необходимо сразу обработать запрос, то " (", release_year, ")")
        это нам даст значение года сразу после названия 
        '''

        select_movies_query = """
        SELECT CONCAT(title, " (", release_year, ")"),
            collection_in_mil
        FROM movies
        ORDER BY collection_in_mil DESC
        LIMIT 5
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
        #--------------------------------------------------------------------
        select_movies_query = """
        SELECT CONCAT(title, " (", release_year, ")"),
            collection_in_mil
        FROM movies
        ORDER BY collection_in_mil DESC
        """
        # В даном примере мы сортируем и выводим пять записей

        '''
        .fetchone() извлекает следующую строку результата в виде кортежа, либо None, 
        если доступных строк больше нет.
        .fetchmany() извлекает следующий набор строк из результата в виде списка кортежей. 
        Для этого ему передается аргумент, по умолчанию равный 1. 
        Если доступных строк больше нет, метод возвращает пустой список.
        '''
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchmany(size=5):
                print(movie)
            cursor.fetchall()
except Error as e:
    print(e)   




