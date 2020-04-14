#!/usr/bin/env python3 m pip install --upgrade flask
import urllib3
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)
app.config["MYSQL_HOST"] = os.environ['MYSQLHOST']
app.config["MYSQL_USER"] = os.environ['MYSQLUSE']
app.config["MYSQL_PASSWORD"] = os.environ['MYSQLPASS']
app.config["MYSQL_DB"] =  os.environ['MYSQLDB']
mysql= MySQL(app)

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://localhost:5000')
    assert 200 == r.status