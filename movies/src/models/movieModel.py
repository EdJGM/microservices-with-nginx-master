from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():
    
    @classmethod
    def get_movies(self):
        try:
            conn = get_connection()
            movies = []

            with conn.cursor() as cursor:
                cursor.execute('SELECT id, titulo, duracion, fecha_estreno FROM movie ORDER BY titulo ASC')
                result = cursor.fetchall()

                for row in result:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())

            conn.close()
            return movies

        except Exception as e:
            raise e
        
    @classmethod
    def get_movie(self, id):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute('SELECT id, titulo, duracion, fecha_estreno FROM movie WHERE id = %s', (id,))
                row = cursor.fetchone()

                movie=None
                if row is not None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie = movie.to_JSON()

            conn.close()
            return movie

        except Exception as e:
            raise e
    
    @classmethod
    def add_movie(self, movie):
        try:
            conn = get_connection()

            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO movie (id, titulo, duracion, fecha_estreno) VALUES (%s, %s, %s, %s)', (movie.id, movie.titulo, movie.duracion, movie.fecha_estreno))
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows

        except Exception as e:
            raise e
        
    @classmethod
    def update_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE movie SET titulo = %s, duracion = %s, fecha_estreno = %s 
                                WHERE id = %s""", (movie.titulo, movie.duracion, movie.fecha_estreno, movie.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_movie(self, movie):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM movie WHERE id = %s", (movie.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)