# This code was written copying Udacity course content and adapted to 
# make this project unique to me. 

import media
import fresh_tomatoes

# code below links to media file 
# inputs specifics of each of the movies in this order: Title, Summary, Art, Youtube trailer

howls = media.Movie(
    "Howls Moving Castle", "A lonely girl's life is changed when she " 
    "befriends a wizard living in a moving castle and she is cursed by an" 
    " evil witch", 
    "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg", #NOQA
    "https://www.youtube.com/watch?v=iwROgK94zcM"
    )

butch = media.Movie(
    "Butch Cassidy and the Sundance Kid", "The story of Wild West outlaws" 
    " Robert LeRoy Parker and Harry Longabaugh who are on the run from a" 
    " crack US posse after a string of train robberies.",
    "https://upload.wikimedia.org/wikipedia/en/f/fd/Butch_sundance_poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=9dxFHc5e9ik"
    )

hero = media.Movie (
    "Hero", "A story of Jing Ke's assassination attempt on the Chinese "
    "King of Quin in 227 BC", 
    "https://upload.wikimedia.org/wikipedia/en/0/08/Hero_poster.jpg", 
    "https://www.youtube.com/watch?v=srFhXDZhUZI"
    )

arrival = media.Movie (
    "Arrival", "A story of a linguist enlisted by the US Army to "
    "discover why aliens have arrived on Earth before tensions lead "
    "to war", 
    "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=tFMo3UJ4B4g"
    )

amelie = media.Movie (
    "Amelie", "A whimsical Parisian movie about a shy waitress who "
    "decides to change the lives of those around her for the better, "
    "while struggling with her own isolation.", 
    "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg", 
    "https://www.youtube.com/watch?v=2UT5xaAfxWU"
    )  

usual = media.Movie (
    "The Usual Suspects", "A small time con man tells a police "
    "interrogator the convoluted story of a recent heist gone wrong "
    "where only he survives", 
    "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg", #NOQA
    "https://www.youtube.com/watch?v=oiXdPolca5w"
    )

water = media.Movie (
    "Like Water for Chocolate", "The story of a girl born youngest of "
    "three and who is obligated to carry on an old family tradition "
    "forsaking love and children in order to care for her mother. "
    "However love, passion and destiny have another life in "
    "store for her", 
    "https://upload.wikimedia.org/wikipedia/en/9/90/Likewaterforchocolate.PNG", #NOQA
    "https://www.youtube.com/watch?v=vb2QJvmETL4")

# code below links to media file & designates display order of movies
movies = [howls, hero, arrival, amelie, usual, water,  butch]  

# code below links to fresh_tomoato file that provides html/css format of the content
fresh_tomatoes.open_movies_page(movies) 
