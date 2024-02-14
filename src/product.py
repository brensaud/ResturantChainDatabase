import json

class Product:
    def __init__(self, product_id, name, description, price, chain_name):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.chain_name = chain_name

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'chain_name': self.chain_name
        }
    
    def save_to_file(self):
        filename = f'{self.product_id}.json'
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)
