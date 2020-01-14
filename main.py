import pymongo
from pymongo import MongoClient
import argparse

cluster = MongoClient("mongodb+srv://admin:admin@cluster0-wtn7j.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["Employee"]

parser = argparse.ArgumentParser(description="To add delete fetch records in Json Structure")
parser.add_argument('--add', help='Add the record in database using ')
parser.add_argument('--delete', help='delete the record in database using key _id')
parser.add_argument('--select', help='select the record in database usind key- _id')
parser.add_argument('--f', help='from all the record in database')
parser.add_argument('--find', help='Find the record in database using using Keys such as _id ')
parser.add_argument('--fetchAll', help='Add the record in database using ')

args = parser.parse_args()
args1 = vars(parser.parse_args())

def add():
    data = args.add
    data_to_dict = eval(data)
    avail = collection.find_one({'_id': data_to_dict['_id']})
    if(avail):
        print('Records with same ID already available')
    else:
        collection.insert_one(data_to_dict)
        print(data)

def delete():
    data = args.delete
    data_to_dict = eval(data)
    avail = collection.find_one({'_id': data_to_dict['_id']})
    if(avail):
        collection.delete_one(data_to_dict)
    else:
        print('record is not available to delete')
    print(collection.count_documents({}))

def find():
    data = args.find
    data_to_dict = eval(data)
    avail = collection.find_one(data_to_dict)
    if(avail):
        print(avail)
    else:
        print("Record is not available To Find")

def fetchAll():
    data = args.fetchAll
    data_to_dict = eval(data)
    result = collection.find(data_to_dict)
    if result:
        for i in result:
            print(i)
    else:
        print("Record with such key is not available")
def select():
    data = args1['select'] 
    data_to_dict = eval(data)
    result = collection.find_one(data_to_dict)
    if(result):
        print(result[args1['f']])
    else:
        raise valueError('id is not available in records')
    
if(args.add):
    add()
if(args.delete):
    delete()
if(args.find):
    find()
if(args.fetchAll):
    fetchAll()
if(args.select):
    select()
