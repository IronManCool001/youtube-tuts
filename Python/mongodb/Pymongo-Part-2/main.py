import pymongo
from pymongo import MongoClient
import dns


client = pymongo.MongoClient("mongodb+srv://<username>:<password>@youtube.vzxa2.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client['test'] #db = client[DBNAME]
collection = db['test'] #collection = db[collection_name]

post1 = {'_id':6,'name':'Technical Friend', 'Subscribers':11}
post2 = {'_id':2,'name':'Edureka', 'Subscribers':'32million'}
post3 = {'_id':1,'name':'Vishnu Joshi','Subscribers': 55}
#collection.insert_one()
#collection.find()