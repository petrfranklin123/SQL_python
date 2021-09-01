from getpass import getpass
from mysql.connector import connect, Error
'''
Чтобы установитть соединение, используем connect()
эта функция принимает три мараметра user, password и host
и возвращает объект MySQLConnection

Все соединения с БД оборачиваются в try except , таким обазом лучше всего можно перехватить данные 

Чтобы закрыть сессию с БД мы используем with as, если не закрыть, то это приведет к ошибкам 
'''

#Пример добавления БД------------------------------------------------------------------- 
try:
    with connect(
        host ="localhost",
        user = "root",
        password = ""
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
        #Строка SQL кода 
        create_db_query = "CREATE DATABASE onlline_movie_rating"
        with connection.cursor() as cursor:
            #Выполнение добавления 
            cursor.execute(create_db_query) 
#если не вышло подключиться, то выводим шибку 
except Error as e:
    print(e)   








