from application import app
import requests
import random


@app.route('/',methods=['GET','POST'])
def output():
    coinflip = random.random()

    if coinflip > 0.5:
        fate = 'good' 
    else:
        fate = 'bad'
    
    return fate