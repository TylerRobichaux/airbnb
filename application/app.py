# flask is module, Flask is class
from flask import Flask, render_template, request #this request is for form data

#import requests  #talks to APIs
#from .models import *
#from dotenv import load_dotenv
#import os

#load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return 'success the flask app is running'

#app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DB_URI']
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#DB.init_app(app) #connects DB w/ flask app obejct



#@app.route('/render')
#def render():
#    return render_template ("some.html")

#@app.route('/vacay_insert/<word>')
#def insert(word):
#    return render_template("insert.html", word=word)

#@app.route('/owner_insert/<word>')
#def insert(word):
#    return render_template("insert.html", word=word)

#@app.route('/vacay_prices/<price>')
#def vacay_prices():
#    return message = requests.get().json()(location recommendations based on price)

#@app.route('/owner_prices/<your_location>')
#def owner_prices():
#    return message = requests.get().json()(price recommendations based on location)

#@app.route('/reset')
#def reset():
    #not for the public
#    DB.drop_all()
#    DB.create_all()
#    return f'DB reset'
