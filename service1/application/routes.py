from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')