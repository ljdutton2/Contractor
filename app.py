from flask import Flask, render_template, request
import requests
from pymongo import MongoClient
import os

client = MongoClient()
db = client.Contractor
products = db.products
app = Flask(__name__)

@app.route('/')
def index():
    return("TEST")

@app.route('/home')
def get_store():
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
