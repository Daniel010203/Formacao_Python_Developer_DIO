import pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("<link no site>")

db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\nRecuperando info da coeção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pyM.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profiles_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Joao'}
]

print("\nColeçÕes armazenadas no MongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# db['posts'].drop() - apagar tudo

posts.delete_one({"author": "mike"}) # deleta um campo expecifico

client.drop_database('<nome do banco de dados>') # deleta banco de dados