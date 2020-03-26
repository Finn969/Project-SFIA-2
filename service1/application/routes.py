from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        details = request.form
        requests.put('http://service_2:5001', data = [details['dob'],details['gender']])
        
   return render_template('home.html')

@app.route('/horoscope', methods=['POST','GET'])
def horoscope():
    response = requests.get('http://service_4:5003/')
    print(response)
    sentence = response.text
    return render_template('output.html',sentence=sentence)