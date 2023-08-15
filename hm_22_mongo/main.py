from hm_22_mongo.collect.orders_collection import Orders
from hm_22_mongo.collect.products_collection import Products

orders = Orders()
orders.insert_one({'product_id': 1, 'quantity': 10.00})
orders.insert_many_data([{'product_id': 2, 'quantity': 5.5},
                         {'product_id': 3, 'quantity': 3.5},
                         {'product_id': 4, 'quantity': 15.00},
                         {'product_id': 5, 'quantity': 12.00}])
print(orders.find_one({'product_id': 1, 'quantity': 10.00}))
print(orders.count_all())
print(orders.count_match({'product_id': 1}))
orders.update_one_data({'product_id': 1}, {'$set': {'product_id': 6}})
orders.delete_one({'product_id': 6})
orders.find_all()

products = Products()
products.drop()
products.insert_many_data([{'name': 'Potato', 'price': 1.00},
                           {'name': 'Orange', 'price': 1.49},
                           {'name': 'Bananas', 'price': 1.39},
                           {'name': 'Water', 'price': 1.25},
                           {'name': 'Bread', 'price': 1.50}])
products.update_many({'name': {'$regex': '^B'}}, {'$set': {'name': 'Milk'}})
products.delete_many({'name': 'Milk'})
products.find_all()
