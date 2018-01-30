# code is written while taking Udacity course and copying the lesson

import webbrowser

class Movie():
    
    #retrieves and stores data about the movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #opens youtube trailer
    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)
        

        
