class Movie:
    """Movie Info Class.Include movie title, movie storyline, poster image and trailer."""
    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.movie_storyline = movie_storyline
        self.title = title
