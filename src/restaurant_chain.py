class RestaurantChain:
    def __init__(self, chain_name, location, phone_number,
                 type,
                 description,
                 local_hours,
                 cuisines,
                 ):
        self.chain_name = chain_name
        self.location = location
        self.phone_number = phone_number
        self.type = type
        self.description = description
        self.local_hours = local_hours
        self.cuisines = cuisines

        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return {
            'chain_name': self.chain_name,
            'location': self.location,
            'phone_number': self.phone_number,
            'type': self.type,
            'description': self.description,
            'local_hours': self.local_hours,
            'cuisines': self.cuisines,
            'products': [product.to_dict() for product in self.products]
        }
