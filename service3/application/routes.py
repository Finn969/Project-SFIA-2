from application import app
from . import generator
from flask import render_template, request, redirect, url_for
import requests

# This service will generate a horoscope, with modifiers to gender and star-signs

@app.route('/', methods=['GET','POST'])
def prediction():
    mood = requests.get('http://service_4:5003')
    horoscope = generator.generate(mood)
    print (horoscope)
    return horoscope