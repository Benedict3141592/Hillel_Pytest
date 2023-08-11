from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    price = Column(FLOAT, nullable=False)

    def __str__(self):
        return f"id: {self.id}\tname: {self.name}\tprice: {self.price}"
