import pymongo
from bson import ObjectId

client = pymongo.MongoClient("localhost", 27017)
db = client["db_prac"]
collection = db["demo"]

def insert_data(data):
    document = collection.insert_one(data)
    return document.inserted_id

def update_data(document_id, data):
    result = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return result.modified_count > 0

def delete_data(document_id):
    result = collection.delete_one({'_id': ObjectId(document_id)})
    return result.deleted_count > 0

def get_data_by_id(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_all_data():
    data = list(collection.find())
    return data

while True:
    print("Menu:")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Get Data by ID")
    print("5. Get All Data")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        data_to_insert = {
            "name": input("Enter Name: "),
            "roll": int(input("Enter Roll: "))
        }
        document_id = insert_data(data_to_insert)
        print(f"Inserted document ID: {document_id}")
    elif choice == '2':
        document_id = input("Enter Document ID to update: ")
        data_to_update = {
            "roll": int(input("Enter New Roll: "))
        }
        update_result = update_data(document_id, data_to_update)
        if update_result:
            updated_document = get_data_by_id(document_id)
            print(f"Updated document: {updated_document}")
        else:
            print("Document not found or not updated.")
    elif choice == '3':
        document_id = input("Enter Document ID to delete: ")
        delete_result = delete_data(document_id)
        if delete_result:
            print("Document deleted.")
        else:
            print("Document not found or not deleted.")
    elif choice == '4':
        document_id = input("Enter Document ID to retrieve: ")
        data = get_data_by_id(document_id)
        if data:
            print(f"Document: {data}")
        else:
            print("Document not found.")
    elif choice == '5':
        all_data = get_all_data()
        print(f"All documents in the collection: {all_data}")
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please select a valid option.")

client.close()
