from application import app
from flask import render_template, request, redirect, url_for
import requests

#This service will generate astrological info from the dob

@app.route('/', methods=['GET','POST'])
def astroinfo():
    starsign = ''
    birthday = requests. 

    # code to determine starsign
    # test output
    starsign = 'Libra'
    return starsign