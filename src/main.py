import os
import json
from pathlib import Path
from restaurant_chain import RestaurantChain
from product import Product
from restaurant_database import RestaurantDatabase
from restaurant_cli import RestaurantCLI
from data_loader import DataLoaderFactory



def main():

    Home_Dir = Path.home()
    Sample_Data_Dir = Path(r"OneDrive - Asia Pacific University\Desktop\ResturantChainDatabase\sample_data")
    Data_Folder_Path = Home_Dir / Sample_Data_Dir
    data_type = 'json'

    data_loader = DataLoaderFactory.create_data_loader(data_type, str(Data_Folder_Path))
    restaurant_data = data_loader.load_data()

    database = RestaurantDatabase()

    for restaurant_info in restaurant_data:
        count = 0
        for data in restaurant_info.get('stores'): # data count according to my knowlede => 100
            for key, value in data.items():
                if key == "_id":
                    print(key, "==> ", value)
                    if key == "8b7894bf-51bd-4b3c-82c8-59c315e81b69":
                        count += 1
                break
            break
        print("count", count)
        break

        # Test for all the

        # test for all data

        # chain_name = restaurant_info['chain_name']
        # location = restaurant_info['location']
        # restaurant_chain = RestaurantChain(chain_name, location)

        # for product_info in restaurant_info['products']:
        #     product_id = product_info['product_id']
        #     name = product_info['name']
        #     description = product_info['description']
        #     price = product_info['price']
        #     product = Product(product_id, name, description, price, chain_name)
        #     restaurant_chain.add_product(product)

        # database.insert_restaurant_chain(restaurant_chain)

    # cli = RestaurantCLI(database)
    # cli.run()

if __name__ == "__main__":
    main()
