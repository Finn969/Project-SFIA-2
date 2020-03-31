from application import app
from flask import render_template, request, redirect, url_for
import requests
import json

@app.route('/', methods=['POST','GET'])
def home():
    default_phrase = 'Please enter your date of birth'
    if request.method == 'POST':
        details = request.form
        DOB = details["dob"]
        print (DOB)

        response = requests.get('http://service_2:5001?DOB='+DOB)
        print (response)
        sentence = response.text
        print (sentence)
        return render_template('home.html',sentence = sentence)
    return render_template('home.html', sentence = default_phrase)

#@app.route('/horoscope', methods=['POST','GET'])
#def horoscope():
#    response = requests.get('http://localhost:5001?')
#    print(response)
#    sentence = response.text
#    print (sentence)
#    return render_template('output.html',sentence=sentence)