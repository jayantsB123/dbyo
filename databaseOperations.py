def insert(c):
    name = input("\nEnter name:")
    age = input("\nEnter age:")
    c.insert_one({"name":name, "age":age})

def del_ete(c):
    name= input("\nEnter name to delete record of :")
    c.delete_many({"name":name})

def upd_ate(c):
    name = input("\nEnter name to have its objects changed:")
    new_name = input("\nEnter new name: ")
    new_age = input("\nEnter new age: ")

    c.update_one({"name": name}, {"$set": {"name": new_name, "age": new_age}})

def menu(c):
    x = input("\n1.Display\n2.Insert\n3.Delete\n4.Update\nEnter input:")
    if x == '1':
        documents = c.find()
        for document in documents:
            pprint(document)
    elif x == '2':
        insert(c)
    elif x == '3':
        del_ete(c)
    elif x == '4':
        upd_ate(c)
    else:
        print("\nInvalid input")
        exit(0)
                

import pymongo
from pprint import pprint
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#database_names = client.list_database_names()
#print(database_names)
#for db_name in database_names:
#print("Database:\n")

db = client['db_prac']
#collections = db.list_collection_names()

#print(collections)
#for collection in collections:
#print(collection," :\n")

c = db['mongo_test']
documents = c.find()

for document in documents:
    pprint(document)
print()

while(1):
    menu(c)