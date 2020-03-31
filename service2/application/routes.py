from application import app, starsign
from flask import render_template, request, redirect, url_for
import requests

#This service will generate astrological info from the dob

@app.route('/', methods=['GET','POST'])
def astroinfo():
    
    birthday = request.args.get('DOB')
    print (birthday)
    # code to determine starsign
    # test output
    zodiac = starsign.starsign(birthday)
    print (zodiac)
    return zodiac