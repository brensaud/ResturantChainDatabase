{
    "stores":[
        {
            '_id',
            'name',
            'phone_number',
            'address',
            'type',
            'description',
            'local_hours',
            'cuisines',

            'food_photos',
            'logo_photos',
            'store_photos',
            'menus',
            'dollar_signs',
            'pickup_enabled',
            'delivery_enabled',
            'offers_first_party_delivery',
            'offers_third_party_delivery',
            'weighted_rating_value',
            'aggregated_rating_count',
            'supports_upc_codes',
            'is_open',
            'menu_id'
        }
    ]
}



# These can be product field 
Item names
Descriptions
Prices
Categories (e.g., appetizers, main courses, desserts)
Dietary information
Availability (e.g., special offers, seasonal items)

{
    "stores": [
        {
            "_id": "store1",
            "name": "Store 1",
            "products_info": [
                {
                    "product_id": "1",
                    "name": "Product 1",
                    "description": "Description of Product 1",
                    "price": 10.99,
                    "photos": ["product1_photo1.jpg", "product1_photo2.jpg"]
                },
                {
                    "product_id": "2",
                    "name": "Product 2",
                    "description": "Description of Product 2",
                    "price": 15.99,
                    "photos": ["product2_photo1.jpg", "product2_photo2.jpg"]
                }
            ]
        },
        {
            "_id": "store2",
            "name": "Store 2",
            "products_info": [
                {
                    "product_id": "3",
                    "name": "Product 3",
                    "description": "Description of Product 3",
                    "price": 12.99,
                    "photos": ["product3_photo1.jpg", "product3_photo2.jpg"]
                },
                {
                    "product_id": "4",
                    "name": "Product 4",
                    "description": "Description of Product 4",
                    "price": 8.99,
                    "photos": ["product4_photo1.jpg", "product4_photo2.jpg"]
                }
            ]
        }
    ]
}

In this modified structure:

Each store object contains a "products_info" field, which is a list of product objects.
Each product object includes fields such as "product_id", "name", "description", "price", and "photos".
The "photos" field is assumed to contain a list of filenames for photos associated with each product.