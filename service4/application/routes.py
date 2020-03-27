from application import app
import requests

# this service will process the outputs from services 2 and 3.

@app.route('/',methods=['GET'])
def output():
    starsign = requests.get('http://localhost:5001/')
    fortune = requests.get('http://localhost:5002/')
    print (starsign, fortune)
    output = "Your star sign is: "+ starsign.text +'/n'+fortune.text
    return output