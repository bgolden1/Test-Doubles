"""
Database: Mongodb
Version: 5.0.3
Port: 27017
Download link: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition
"""

from pymongo import MongoClient


class Program2:
    def __init__(self):
        connection_string = 'mongodb://localhost'
        client = MongoClient(connection_string)
        db = client.get_database('local')
        self.customers = db['customers']
        self.orders = db['orders']

    def create_customer(self, _id, name, num_goods_purchased):
        customer = {
            '_id': _id,
            'name': name,
            'num_goods_purchased': num_goods_purchased
        }
        self.customers.insert_one(customer)

    def create_order(self, customer_id, num_goods_purchased):
        order = {
            'customer_id': customer_id,
            'num_goods_purchased': num_goods_purchased
        }
        self.orders.insert_one(order)

    def get_customers(self):
        return_list = []
        for customer in self.customers.find():
            return_list.append(customer)
        return return_list
