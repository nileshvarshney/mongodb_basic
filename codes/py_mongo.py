import pymongo
from urllib.parse import quote_plus
import fake

# connect to mongodb
# uri = "mongodb://%s:%s@%s:27017" % (quote_plus("root"), quote_plus("password"), "localhost")
uri = "mongodb://%s:%s@%s:27017" % (quote_plus("root"), quote_plus("password"), "mongodb")
client = pymongo.MongoClient(uri)

db = client.mymongo
# check the existance of the database
if  db.name not in client.list_database_names():
    print(db.name + " already exists.....")

students = db["students"]
collection_list = db.list_collection_names()

data = fake.get_student_dake_data(10)
students.insert_many(data)
students.insert_many(fake.get_student_dake_data(10, "hi_IN"))
# print(data)
# for  d in data:
#     x = students.insert_one(d)
#     print(d)

# x = students.find_one()
# print(x)