from application import app
from flask import render_template, request, redirect, url_for
import requests

# This service will generate a horoscope, with modifiers to gender and star-signs

@app.route('/', methods=['GET','POST'])
def prediction():
    horoscope = 'You will struggle to complete a difficult task'
    print (horoscope)
    return horoscope