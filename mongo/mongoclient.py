from pymongo import MongoClient

class MongoConnect(object):
    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=27017)
        self.collection = client['test']['stu']

    def insert(self):
        pass