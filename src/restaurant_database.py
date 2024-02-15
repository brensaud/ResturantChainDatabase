from pymongo import MongoClient


class RestaurantDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['restaurant_db']
        self.restaurant_collection = self.db['restaurants']

    def insert_restaurant_chain(self, restaurant_chain, product_folder_path):
        restaurant_doc = restaurant_chain.to_dict()
        restaurant_id = self.restaurant_collection.insert_one(restaurant_doc).inserted_id

        for product in restaurant_chain.products:
            product.save_to_file(product_folder_path)
            self.restaurant_collection.update_one(
                {'_id': restaurant_id},
                {'$addToSet': {'product_files': f'{product.product_id}.json'}}
            )
    
    def search_product(self, product_id):
        product = self.product_collection.find_one({'product_id': product_id})
        return product
