from application import app
from flask import render_template, request, redirect, url_for
import requests
import json

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        details = request.form
        DOB = details["dob"]
        DOB = json.dumps(DOB)
        print (DOB)

        requests.post('http://localhost:5001', json=DOB)
        return redirect(url_for('horoscope'))
    return render_template('home.html')

@app.route('/horoscope', methods=['POST','GET'])
def horoscope():
    response = requests.get('http://service_4:5003/')
    print(response)
    sentence = response.text
    print (sentence)
    return render_template('output.html',sentence=sentence)