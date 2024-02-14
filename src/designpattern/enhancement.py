"""
Here are some strategies to efficiently handle large amounts of data in this restaurant database application:

    1. Indexes
        - Create indexes on frequently queried fields like product ID, chain name, etc. 
        - This will optimize search queries on those fields.

    2. Pagination
        - When displaying results, use pagination rather than retrieving all matching documents. 
        - Fetch and display a limited number of results per page.

    3. Data Streaming
        - For large imports or exports, stream the data rather than loading fully in memory. 
        - Write/read to MongoDB in chunks to reduce memory usage.

    4. Compression
        - Store large product details JSONs as compressed files to optimize disk usage. 
        - Decompress only when accessed.

    5. Caching
        - Use Redis or Memcached to cache frequently accessed queries and results.
        - This avoids hitting the database for identical queries.

    6. Sharding 
        - For massive data, enable auto-sharding in Atlas to distribute data across machines.

    7. Serve Static Files
        - Serve large static assets like images from a separate service like S3 or CDN.

The combination of above strategies can allow the application to scale efficiently for large datasets.
"""


"""


The key points:
    Index on product_id
    Caching with Redis
    Pagination for API requests
    Streaming chunked data loading
    Serving paginated data as JSON API

    Indexes and caching with Redis
    Chunked data loading
    Print product search results
    Pagination helper method
"""

"""
import json
from pymongo import MongoClient, ASCENDING
from bson.json_util import dumps
from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379)

class RestaurantDB:

  def __init__(self):
    self.client = MongoClient('mongodb://localhost:27017/')
    self.db = self.client['restaurantDB']
    self.db.products.create_index([('product_id', ASCENDING)])

  def load_data(self): 
    # stream and chunk data loading 
    
  def search_product(self, product_id):
    # first check cache
    product = cache.get(product_id)
    if not product:
      product = self.db.products.find_one({'_id': product_id})
      cache.set(product_id, dumps(product)) 
    
    # return paginated result
    output = dumps(product) 
    return jsonify({'data': output})

# pagination example
@app.route('/products') 
def get_products():
  page = int(request.args.get('page', 1))
  per_page = 10
  products = db.products.find().skip((page-1)*per_page).limit(per_page)
  return jsonify(products)

if __name__ == '__main__':
  db = RestaurantDB()
  db.load_data()
  app.run(debug=True)
"""



"""
import json 
from pymongo import MongoClient, ASCENDING
from bson.json_util import dumps
import redis

class RestaurantDB:

  def __init__(self):
    self.client = MongoClient('mongodb://localhost:27017/')
    self.db = self.client['restaurantDB']  
    self.db.products.create_index([('product_id', ASCENDING)])
    self.cache = redis.Redis(host='localhost', port=6379)

  def load_data(self):
    # read data in chunks
   
  def search_product(self, product_id):
    product = self.cache.get(product_id)
    if not product:
      product = self.db.products.find_one({'_id': product_id})
      self.cache.set(product_id, dumps(product))

    print(f"Name: {product['name']}")
    print(f"Description: {product['description']}")
    print(f"Price: {product['price']}")
    print(f"Chain: {product['chain']}")
        
# Helper method for pagination
def get_page(cursor, page_num, page_size):
  start = (page_num - 1) * page_size
  end = start + page_size
  output = []
  for i, doc in enumerate(cursor):
    if i >= start and i < end:
      output.append(doc)
  return output 

# Usage
db = RestaurantDB()
db.load_data()

product_id = input("Enter product ID: ")
db.search_product(product_id)

# Pagination
page_num = int(input("Enter page number: "))
page_size = 10
products = db.db.products.find()
results = get_page(products, page_num, page_size)
print(results)
"""