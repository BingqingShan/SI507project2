# Instructions
## What this program can do
This program consists of 5 other files other than this Readme.md file.By running the flask app (written in SI507_project2.py), you will see how many movies are recorded in the csv file and will list 5 movie titles and their corresponding ratings through following specific routes. The movie list will change each time you refresh the url. The diagram.jpg represents the relationship of part of the data in the movies_clean.csv file.


The movies_tools.py helps read the csv file and creates the class you need to run the flask app. The class called movie is the one this app will need in this file.


The SI507_project2.py can tie the code in movies_tools.py into a Flask application. It will allow you to go to the routes at the specific paths and show the relevent result on the HTML page. Remember, if you are going to a route which is not defined in the program, you may run into error. So limit your routes in the following options, unless you want to add more routes yourself:

1. / (home page)
2. /movies/ratings/

## Dependencies the project relies on
Thus, to guarantee everyone can run this program properly, you may install all the required packages which is written in requirements.txt.

How to install it:

once you set up your virtual environment, you can type in $ pip install -r requirements.txt to install all the required packages all at once.

## How to run this app
Once you download the folder, in your terminal, set up your virtual environment and install packages as said above. Once you are done with that, you can cd to the file SI507_project2.py, type in python SI507_project_2.py runserver in your terminal and then let it run. You will see a builtin server (eg. http://127.0.0.1:5000). copy paste it in your web browser and then you will see the homepage with numbers of movies recorded in the csv file. Now you can go ahead and start to play around with different routes now.
