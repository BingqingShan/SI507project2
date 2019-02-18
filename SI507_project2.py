from flask import Flask
from movies_tools import *

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>'+total_number+' movies recorded.</h1>'


# @app.route('/')
# def home():
#     return 'Welcome to the banking application!'
#
# @app.route('/bank/<name>')
# def bankname(name):
#     bank_name= Bank(name,Dollar)
#     return 'Welcome to '+ bank_name.name +'!'
#



if __name__ == '__main__':
    app.run()
