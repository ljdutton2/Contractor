from pymongo import MongoClient
from bson.objectid import ObjectId


#dummy (ish) data used to display products 
product_1 =  {
     "name": "Spider Plant",
 "picture": 'static/Houseplants_SpiderPlant.jpeg',
 "price": "3.99",
 "difficulty": "Easy"
 }

product_2 = {
    "name": "Yellow Tulip",
 "picture":"static/tulip.jpeg",
 "price": "8.99",
 "difficulty": "hard"
 }

product_3 = {
    "name": "Assorted Succulents",
 "picture":"static/succulent.jpeg" ,
 "price": "1.99",
 "difficulty": "Easy"
 }

product_4 = {
    "name": "Sunflowers",
 "picture": "static/sunflower.jpeg",
 "price": "10.00",
 "difficulty": "Medium" }

product_5 = {
    "name": "Bonsai Tree",
 "picture": "static/bonsai.jpeg",
 "price": "12.99",
 "difficulty": "Very Difficult"
 }  


product_list = [
    product_1,
    product_2,
    product_3,
    product_4,
    product_5
]
#class to create the store by adding to mongodb
class Store():
    def __init__(self, product):
         self.product = product
    
    def show_product(self):
         self.product.delete_many({})
        
         self.product.insert_many(product_list)
        
         for i in self.product.find():
             print(product_list)