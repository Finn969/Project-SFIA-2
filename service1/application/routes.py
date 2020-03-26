from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['POST'])
def home():
    return render_template('home.html')

@app.route('/horoscope', methods=['GET'])
def horoscope():
    response = requests.get('http://service_4:5003/')
    print(response)
    sentence = response.text
    return render_template('output.html',sentence=sentence)