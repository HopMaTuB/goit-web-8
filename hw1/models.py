import mongoengine as me
import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sunkiper:04101993Qwe@cluster1.7bztefj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# Create a new client and connect to the server

client = MongoClient(uri, server_api=ServerApi('1'))
# client = MongoClient(uri, tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

me.connect(host=uri)


class Author(me.Document):
    name = me.StringField(required=True)
    meta = {'collection': 'authors'}

class Quote(me.Document):
    content = me.StringField(required=True)
    author = me.ReferenceField(Author, required=True)
    tags = me.ListField(me.StringField())
    meta = {'collection': 'quotes'}
