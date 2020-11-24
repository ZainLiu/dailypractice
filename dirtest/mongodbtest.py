import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
collection = myclient["test"]['stu']
all_stu = collection.find()
for i in all_stu:
    print(type(i),i)