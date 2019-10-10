from flask import Flask, render_template, request, redirect, url_for
import requests
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from pprint import pprint
#from plant_list import Store

app = Flask(__name__)
FLASK_APP = app


host = os.environ.get('MONGODB_URI', 'mongodb://127.0.0.1:27017/Contractor')
client = MongoClient(host=host)
db = client.get_default_database()
products = db.plant_list


    


@app.route('/',methods=['GET'])
def show_home():
    if request.method == 'GET':
        items = products.find()
        plants = []
     
        for x in items:
            plants.append(x)
            print(x["_id"]) 
        return render_template('all_products.html', product_list=plants)

@app.route('/plants', methods=['GET', 'POST'])
def plants_submit():
    """Submit a new plant."""
    plant = {
        'name': request.form.get('name'),
        'picture': request.form.get('picture'),
        'price': request.form.get('price'),
        'difficulty': request.form.get('difficulty'),
        'created_at': datetime.now()
    }
    print(plant)
    plant_id = plant.insert_one(plant).inserted_id
    return redirect(url_for('new_plant.html', plant_id=plant_id))

@app.route('/plants/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('new_plant.html',product={})



@app.route('/products/<product_id>')
def products_show(product_id):
    print(product_id)
    product = products.find_one({'_id':ObjectId(product_id)})
    print(product)
    return render_template('products_show.html', product=product)

#delete route#



@app.route('/test', methods=['GET'])
def test():
    return "hi"




if __name__ == '__main__':
    app.run(debug=True)
