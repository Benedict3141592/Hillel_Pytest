from hm_20_sql_alchemy.models.orders import Orders, Base
from hm_20_sql_alchemy.session_db import session, engine


class OrdersRepository:
    def __init__(self):
        self.__session = session

    @staticmethod
    def create_table_orders():
        Base.metadata.create_all(engine)

    def get_by_id(self, id_value: int):
        order = self.__session.get(Orders, {"id": id_value})
        return order

    def get_all(self):
        all_orders = self.__session.query(Orders).all()
        for order in all_orders:
            print(f"\n{order}")
        return all_orders

    def insert_one(self, order: Orders):
        self.__session.add(order)
        self.__session.commit()

    def insert_all(self, orders_data):
        for order in orders_data:
            orders = Orders(**order)
            self.__session.add(orders)
            self.__session.commit()
