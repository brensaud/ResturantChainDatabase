# Remove duplicates
unique_restaurants = {}
for data in restaurant_data:
    key = (data['chain_name'], data['location'])
    if key not in unique_restaurants:
        unique_restaurants[key] = data

# Process data
restaurants = []
for key, data in unique_restaurants.items():
    restaurant = Restaurant(data['chain_name'], data['location'])
    for product_data in data['products']:
        product = Product(product_data['product_id'], product_data['name'], product_data['description'], product_data['price'])
        restaurant.add_product(product)
    restaurants.append(restaurant)
