from application import app
import requests
import random

# this service will process the outputs from services 2 and 3.

@app.route('/',methods=['GET','POST'])
def output():
    coinflip = random.random()

    if coinflip > 0.5:
        fate = 'good' 
    else:
        fate = 'bad'
    
    return fate