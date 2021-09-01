from getpass import getpass
from mysql.connector import connect, Error

#запрашиваем id фильма
movie_id = input("Enter movie id: ")
#запрашиваем id пользователя
reviewer_id = input("Enter reviewer id: ")
#Выставляем желаемый рейтинг 
new_rating = input("Enter new rating: ")
update_query = """
UPDATE
    ratings
SET
    rating = "%s"
WHERE
    movie_id = "%s" AND reviewer_id = "%s";

SELECT *
FROM ratings
WHERE
    movie_id = "%s" AND reviewer_id = "%s"
""" % (
    new_rating,
    movie_id,
    reviewer_id,
    movie_id,
    reviewer_id,
)

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "",
        database="onlline_movie_rating",
    ) as connection:
        with connection.cursor() as cursor:
            #multi служит для того, чтобы передавать несколько запросов в базу данных 
            for result in cursor.execute(update_query, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()
except Error as e:
    print(e)


