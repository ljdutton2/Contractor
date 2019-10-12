from flask import Flask, render_template, request, redirect, url_for
import requests
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from pprint import pprint
from datetime import datetime
from plant_list import Store

app = Flask(__name__)
FLASK_APP = app


host = os.environ.get('MONGODB_URI','mongodb://127.0.0.1:27017/Contractor')
print('This is the host' + host)
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
products = db.plant_list

#product=Store(product_list)
#product.show_product()   


@app.route('/',methods=['GET'])
def show_home():
    if request.method == 'GET':
        items = products.find()
        plants = []
     #adding the seperate file of hardcoded inventory to an empty list called plants
        for x in items:
            plants.append(x)
            print(x["_id"]) 
        return render_template('all_products.html', product_list=plants)

@app.route('/plants', methods=['POST'])
def plants_submit():
    """Submit a new plant."""
    #creating a form so the user is able to add new plants
    plant = {
        'name': request.form.get('plant-name'),
        'description': request.form.get('plant-description'),
        'plant-price': request.form.get('plant-price'),
        'difficulty': request.form.get('difficulty'),
       
    }
    print(plant)
    plant_id = products.insert_one(plant).inserted_id
    return redirect(url_for('show_home', plant_id=plant_id))

@app.route('/plants/new')
def plants_new():
    return render_template('new_plant.html', plant={})


@app.route('/plants/<plant_id>')
def products_show(plant_id):
    print(plant_id)
    #necessary mongodb command to gather by the ID
    product = products.find_one({'_id': ObjectId(plant_id)})
    print(product)
    return render_template('products_show.html', product=product)

@app.route('/plants/<plant_id>/delete')
# to remove individual plant from main 
def plants_delete(plant_id):
    print(plant_id)
    product = products.delete_one({'_id': ObjectId(plant_id)})
    print(product)
    return redirect(url_for('show_home', product=product))

   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
