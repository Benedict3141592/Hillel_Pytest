from hm_22_mongo.session_mongo import mydb


class BaseMongo:
    def __init__(self, collection_name):
        self.my_db = mydb
        self.my_collection = self.my_db[collection_name]

    def insert_one(self, data):
        return self.my_collection.insert_one(data)

    def insert_many_data(self, data):
        return self.my_collection.insert_many(data)

    def find_one(self, request):
        return self.my_collection.find_one(request)

    def find_all(self):
        cursor = self.my_collection.find()
        for item in cursor:
            print(item)
        return cursor

    def count_all(self):
        return self.my_collection.count_documents(filter={})

    def count_match(self, request):
        return self.my_collection.count_documents(request)

    def update_one_data(self, old_data, update):
        return self.my_collection.update_one(old_data, update)

    def update_many(self, old_data, update):
        return self.my_collection.update_many(old_data, update)

    def delete_one(self, request):
        return self.my_collection.delete_one(request)

    def delete_many(self, request):
        return self.my_collection.delete_many(request)

    def drop(self):
        return self.my_collection.drop()
