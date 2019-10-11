from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app



sample_inventory_id = ObjectId('5d55cffc4a3d4031f42827a2')

sample_inventory = {
        'name': 'Magnolia',
        'description': 'purple',
        'plant-price': '3.99',
        'difficulty': 'Hard to care for',
}
sample_inventory_form_data = {
      'name': sample_inventory['name'],
        'description': sample_inventory['description'],
        'plant-price': sample_inventory['plant-price'],
        'difficulty': sample_inventory['difficulty']
}





class Testcontractor(TestCase):
    def setUp(self):
        #sets up flask test 
        self.client = app.test_client()

        #used to display erros in flask during tests
        app.config['TESTING'] = True

    def test_all_products(self):
        #to check the inital page w listed products
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_products_show(self):
        #check that plant ID route renders products_show
        #uses the sample ID to test
        result = self.client.get('/plants/5d55cffc4a3d4031f42827a2')
        self.assertEqual(result.status, '200 OK')
    #this is incomplete and doesnt function whatsoever
    #def test_delete_plant(self):
        #checks the delete function
        #result = self.client.get('/plants/5d55cffc4a3d4031f42827a2/delete')
        #self.assertEqual(result.status, '200 OK')
        
    
   
    
        

        








if __name__ == '__main__':
    unittest_main()
