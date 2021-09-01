from getpass import getpass
from mysql.connector import connect, Error
'''
Чтобы установитть соединение, используем connect()
эта функция принимает три мараметра user, password и host
и возвращает объект MySQLConnection

Все соединения с БД оборачиваются в try except , таким обазом лучше всего можно перехватить данные 

Чтобы закрыть сессию с БД мы используем with as, если не закрыть, то это приведет к ошибкам 
'''

#Пример подключения в существующей БД----------------------------------------------------

try:
    with connect(
        host ="localhost",
        user = "root",
        password = "root",
        #Дополнительным параметром бросаем название базы данных 
        database = "onlline_movie_rating"
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
        print(connection)
#если не вышло подключиться, то выводим шибку 
except Error as e:
    print(e)   








