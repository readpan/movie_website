import movie
import fresh_tomatoes
import sqlite3

# connect database
conn = sqlite3.connect('data.db')
# create a cursor object. This can handle SQL.
c = conn.cursor()
# Search movies info from database.
sql_rows = c.execute("SELECT * FROM MovieInfo")
# Initialize Movie instances and put them in "movies" list
movies = []
for i in sql_rows:
    movies.append(movie.Movie(i[1], i[2], i[3], i[4]))
# call fresh_tomatoes class function to render website.
fresh_tomatoes.open_movies_page(movies)
