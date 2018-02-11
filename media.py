"""
Code is written while taking Udacity course and
copied and adapted from the lesson
"""

import webbrowser

class Movie():
    """
    The class stores information about movies title, storyline,
    movie poster, youtube trailer
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Constructor to store data about the movie that user inputs.
        Handles for user to use to operate the movie data.
        Ex. movie_name.title
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens youtube trailer when given movie name.
        Ex. movie_name.show_trailer().
        """
        webbrowser.open(self.trailer_youtube_url)
        
