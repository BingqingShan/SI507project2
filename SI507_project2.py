from flask import Flask
from movies_tools import *

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>'+str(total_number)+' movies recorded.</h1>'

@app.route('/movies/ratings/')
def detail():
    list_movie=''
    for i in range(5):
        detail=Movie()
        list_movie= list_movie+ detail.title+' | '+detail.rating+'<br>'
    return list_movie


if __name__ == '__main__':
    app.run()
