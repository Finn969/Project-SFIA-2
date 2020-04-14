from application import app
from flask import render_template, request, redirect, url_for
import requests
import json
import os
import datetime
app.config["MYSQL_HOST"] = os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASS']
app.config["MYSQL_DB"] = os.environ['MYSQLDB2']


@app.route('/', methods=['POST','GET'])
def home():
    default_phrase = 'Please enter your date of birth'
    default_fortune = 'You will then recieve a horoscope'
    if request.method == 'POST':
        details = request.form
        DOB = details["dob"]

        response = requests.get('http://service_2:5001?DOB='+DOB)
        sentence = response.text

        reply = requests.get('http://service_3:5002')
        message = reply.text

        store = details["saved"]
        if store == 'yes':
            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO horoscopes(dob,starsign,horoscope,time_entered) VALUES(%s,%s,%s,%s)")(DOB,sentence,message,datetime.datetime.now())
            mysql.connection.commit()

        return render_template('home.html',sentence = sentence, fortune = message, date_entered=DOB)
    return render_template('home.html', sentence = default_phrase, fortune = default_fortune)

#@app.route('/horoscope', methods=['POST','GET'])
#def horoscope():
#    response = requests.get('http://localhost:5001?')
#    print(response)
#    sentence = response.text
#    print (sentence)
#    return render_template('output.html',sentence=sentence)

