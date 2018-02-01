# Code is written while taking Udacity course
# and copied and adapted from the lesson
import webbrowser


# Retrieves and stores movie data
class Movie():

    """Stores data about the movie that user inputs."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        """Handles for user to use to operate the movie data."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """Opens youtube trailer."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

        
