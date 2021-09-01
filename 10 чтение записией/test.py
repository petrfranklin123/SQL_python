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
    #огранициваем количество записей до пяти 
        select_movies_query = "SELECT * FROM movies LIMIT 5"
        with connection.cursor() as cursor:
            #выполняем запрос 
            cursor.execute(select_movies_query)
            #записываем результат в переменную
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)   




