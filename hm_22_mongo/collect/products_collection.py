from hm_22_mongo.utilities.baseMongo import BaseMongo


class Products(BaseMongo):
    def __init__(self):
        super().__init__('products')
