from application import app
from . import generator
from flask import render_template, request, redirect, url_for
import requests

# This service will generate a horoscope, with modifiers to gender and star-signs

@app.route('/', methods=['GET','POST'])
def prediction():
    horoscope = generator.generate()
    print (horoscope)
    return horoscope