#!/usr/bin/env python3 m pip install --upgrade flask
from flask import Flask, request
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)
mysql= MySQL(app)
from application import routes