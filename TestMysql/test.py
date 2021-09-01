import copy
from getpass import getpass
from mysql.connector import connect, Error

#person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 
#'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'],
#'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}

'''
#словарь, где указаны объекты, которые были найдены на видео 
slovar = {'car' : 'машина', 'bus' : 'автобус', 'bike' : 'велосипед', 'person' : 'человек'}

#строка тегов, которая будет прередана в sql запрос 
string_query = ""

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "",
        database="onlline_movie_rating",
    ) as connection:
        select_movies_query = """
        SELECT teg FROM tegs
        WHERE id = 1
        """
        #В буфере хранится изначальный вариант ячейки БД
        bufer = ""
        with connection.cursor() as cursor:
            #выполнение SQL запроса 
            cursor.execute(select_movies_query)
            #преобразуем кортеж в данные 
            for movie in cursor.fetchall():
                #преобразуем кортеж в строку
                movie = str(movie)
                #преобразование строки к нижнему регистру
                movie = movie.lower()
                #заменяем пробелы пустой строкой 
                movie = movie.replace(' ', '')  
                movie = movie.replace(')', '') 
                movie = movie.replace('(', '')    
                movie = movie.replace("'", '')  
                #сплитуем строку в массив  
                bufer = movie.split(',')
            #print("-----------------")
            #print(bufer)
            #print(slovar)
            #размерность словаря
            #print(len(slovar))

            #Дублируем массив с БД
            copy_bufer = copy.copy(bufer)
            #print(copy_bufer)

            
            #извлекаем каждое слово из словаря и будем сравнивать 
            for slovo in slovar:
                #print("-----------")
                #print(slovar[slovo])
                #print(bufer)
                iterr = 0
                #print(bufer.index(slovar[slovo]))
                print(slovar[slovo] in bufer)
                
                #находим недостающие элементы в БД и добавляем 
                if (slovar[slovo] in bufer) == False:
                    copy_bufer.append(slovar[slovo])
                    
            print(copy_bufer)

            #создаем строку для запроса 
            for teg in copy_bufer:
                string_query += str(teg)
                string_query += ", "

            print(string_query)

except Error as e:
    print(e)

try:
    with connect(
        host ="localhost",
        user = "root",
        password = "",
        #Дополнительным параметром бросаем название базы данных 
        database = "onlline_movie_rating"
#объект MySQLConnection хрнится в переменной connection
    ) as connection:
    # изменяем название фамилии 
        update_query = """
        UPDATE
            tegs
        SET
            teg = "%s"
        WHERE
            id = 1
        """ % (
            string_query
        )
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()

except Error as e:
    print(e)   
'''


#Блок кода, где будет формироваться словарь для работы с вехним кодом 
#изначальный словарь (эталонный)
slovar = {'car' : 'машина', 'bus' : 'автобус', 'bike' : 'велосипед', 'person' : 'человек'}

#Массив элементов, что нашла нейросеть
arrKeys = ['car', 'bus', 'driver']

#конечный словарь, который пойдет на вход предидущей программы 
endSlovar = {}

#блок кода для сравнение, чтобы не допускать неизвестных слов 
for k, v in slovar.items():
    for key in arrKeys:
        if k == key:
            endSlovar[k] = v

print(endSlovar)