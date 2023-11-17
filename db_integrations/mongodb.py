from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://gigachad:9HTHmV3qa-!Xe25@dlorgcluster.249hybe.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print('Pinged nice')
except Exception as e:
    print(e)
