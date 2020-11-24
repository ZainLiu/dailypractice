from pymongo import MongoClient
client = MongoClient(host="192.168.32.133",port=27017)
collection = client["test"]["stu"]
ret = collection.insert_one({"name":"test10010","age":33,"hometown":"beijing","gender":True})
print(ret)