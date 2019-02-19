from flask import Flask
from movies_tools import *
#my goal is to create 2 routes in this flask app. In one of the routes, it will show the total number of the movies in the movies_clean.csv. In another route, it will randomly print out 5 movies and their ratings accordingly.

app = Flask(__name__)

#homepage route
@app.route('/')
def home():
    return '<h1>'+str(total_number)+' movies recorded.</h1>' #show the number of movies in csv file

#movie and rating route
@app.route('/movies/ratings/')
def detail():
    list_movie=''
    for i in range(5): #show 5 result
        detail=Movie() #call function
        list_movie= list_movie+ detail.title+' | '+detail.rating+'<br>'
    return list_movie


if __name__ == '__main__':
    app.run()
