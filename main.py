import movie
import fresh_tomatoes

# movie instances
jordan = movie.Movie("JORDAN Official Trailer #1 (2018)",
                     "Michael Jordan Biopic Movie Trailer HD",
                     "http://heightandweights.com/wp-content/uploads/2016/01/rs_634x1141-140613051823-634.Michael-Jordan-JR-61314.jpg",
                     "https://www.youtube.com/watch?v=C9aAWKTjG2A")
inception = movie.Movie("InceptionInception (2010) Official Trailer #1",
                        "Christopher Nolan Movie HD",
                        "https://www.warnerbros.com/sites/default/files/styles/juicebox_medium/public/inception_posterlarge_0-587516945.jpg?itok=6RMGrVuA",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0"
                        )
wlk = movie.Movie("Wrath of the Lich King",
                  "This is the official cinematic trailer for World of Warcraft's second expansion, Wrath of the Lich King.",
                  "https://assets.rpgsite.net/images/images/000/003/680/original/World_Of_Warcraft_Wrath_Of_The_Lich_King_01_artwork.jpg",
                  "https://www.youtube.com/watch?v=BCr7y4SLhck")

movies = [jordan, inception, wlk]
fresh_tomatoes.open_movies_page(movies)
