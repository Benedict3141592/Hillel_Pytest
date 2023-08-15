from sqlalchemy.orm import declarative_base, relationships
from sqlalchemy import Column, INTEGER, FLOAT, ForeignKey

from hm_20_sql_alchemy.models.products import Products

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey(Products.id))
    quantity = Column(FLOAT, nullable=False)

    def __str__(self):
        return f"id: {self.id}\tproduct_id: {self.product_id}\tquantity: {self.quantity}"
