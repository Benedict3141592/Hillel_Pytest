from hm_20_sql_alchemy.repositories.orders_repository import OrdersRepository
from hm_20_sql_alchemy.repositories.products_repository import ProductsRepository

products_repo = ProductsRepository()
orders_repo = OrdersRepository()

products_repo.create_table_products()
orders_repo.create_table_orders()

products_data = [
    {'name': 'Potato', 'price': 1.00},
    {'name': 'Orange', 'price': 1.49},
    {'name': 'Bananas', 'price': 1.39},
    {'name': 'Water', 'price': 1.25},
    {'name': 'Bread', 'price': 1.50},
]

products_repo.insert_all(products_data)

orders_data = [
    {'product_id': 1, 'quantity': 10.00},
    {'product_id': 2, 'quantity': 5.5},
    {'product_id': 3, 'quantity': 3.5},
    {'product_id': 4, 'quantity': 15.00},
    {'product_id': 5, 'quantity': 12.00},
]

orders_repo.insert_all(orders_data)

product = products_repo.get_all()
orders = orders_repo.get_all()

print(products_repo.select_info())

c = 0
