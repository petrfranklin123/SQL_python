from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "",
        database="onlline_movie_rating",
    ) as connection:
        select_movies_query = """
        SELECT reviewer_id, movie_id FROM ratings
        WHERE reviewer_id = 2
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)

        delete_query = "DELETE FROM ratings WHERE reviewer_id = 2"
        with connection.cursor() as cursor:
            cursor.execute(delete_query)
            connection.commit()
except Error as e:
    print(e)


