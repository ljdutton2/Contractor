from flask import Flask, render_template, request
import requests
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from pprint import pprint



host = os.environ.get('MONGODB_URI', 'mongodb://127.0.0.1:27017/Contractor')
client = MongoClient(host=host)
db = client.Contractor
products = db.products



app = Flask(__name__)
FLASK_APP = app

images = [
 "http://cdn.shopify.com/s/files/1/0038/9405/0868/products/Houseplants_SpiderPlant_Bonnie_6in_1024x1024.jpg?v=1552591517",
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIgg5hzQ3VuR68NZCqyTkSXpfz19BF5Z4Bs9ZxmBBX9Svfx2N7vA&s',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS7wiQCWofg7KKLvQNU-4ujGoTVBYHUQ-KUyzHCSyWE_Lup-Wn&s',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY7bXTlRvTj5RWE1u9sTDE3Y4TVI_YeJ3S07KDIBpGeF4XtFra&s',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6pW5rc--yKDwkD0q3xFiI3R0o2NrK9kUg32SHBUuqvbCG6YGw&s'
]

plants = [
 {"name": "Spider Plant",
 "picture": images[0],
 "price": "3.99",
 "difficulty": "Easy"},  
 {"name": "Yellow Tulip",
 "picture": images[1],
 "price": "8.99",
 "difficulty": "hard"},  
 {"name": "Assorted Succulents",
 "picture": images[2],
 "price": "1.99",
 "difficulty": "Easy"},  
 {"name": "Sunflowers",
 "picture": images[3],
 "price": "10.00",
 "difficulty": "Medium"},  
 {"name": "Bonsai Tree",
 "picture": images[0],
 "price": "12.99",
 "difficulty": "Very Difficult"},   
]


@app.route('/')
def show_home():
    return render_template('main_page.html', products=products)


@app.route('/view')
def get_store():
    for plant in plants:
        products.insert_one(plant)
        return render_template('all_products.html', products=products.find())


@app.route('/products/<product_id>')
def products_show(product_id):
    product = products.find_one({'_id':ObjectId(product_id)})
    return render_template('products_show.html', product=product)






if __name__ == '__main__':
    app.run(debug=True)
