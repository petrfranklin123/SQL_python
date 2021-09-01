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
        #Чтобы узнать названия пяти фильмов с самым высоким рейтингом
        select_movies_query = """
        SELECT title, AVG(rating) as average_rating
        FROM ratings
        INNER JOIN movies
            ON movies.id = ratings.movie_id
        GROUP BY movie_id
        ORDER BY average_rating DESC
        LIMIT 5
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
        
        print("-------------------------------")

        #CONCAT для объединения строк

        #Найти имя рецензента, давшего наибольшее количество оценок
        
        select_movies_query = """
        SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
        FROM reviewers
        INNER JOIN ratings
            ON reviewers.id = ratings.reviewer_id
        GROUP BY reviewer_id
        ORDER BY num DESC
        LIMIT 1
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)

except Error as e:
    print(e)   




