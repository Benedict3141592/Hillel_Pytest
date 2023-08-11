from hm_20_sql_alchemy.models.orders import Orders
from hm_20_sql_alchemy.models.products import Products, Base
from hm_20_sql_alchemy.session_db import session, engine


class ProductsRepository:
    def __init__(self):
        self.__session = session

    @staticmethod
    def create_table_products():
        Base.metadata.create_all(engine)

    def get_by_id(self, id_value: int):
        product = self.__session.get(Products, {"id": id_value})
        return product

    def get_all(self):
        all_products = self.__session.query(Products).all()
        for product in all_products:
            print(f"\n{product}")
        return all_products

    def insert_one(self, product: Products):
        self.__session.add(product)
        self.__session.commit()

    def insert_all(self, products_data):
        for product in products_data:
            products = Products(**product)
            self.__session.add(products)
            self.__session.commit()

    def select_info(self):
        result = session.query(Products.name, Products.price, Orders.quantity,
                               (Products.price * Orders.quantity)).join(Orders, Products.id == Orders.product_id).all()
        return result
