import pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("<link no site>")

db = client.test
collection = db.test_collection

print(db.test_collection)

# definição de infos para compor o doc
post = {
    "author": "Mike",
    "text": "My first MongoDB application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow(),
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow(),
    },
    {
    "author": "Joao",
    "text": "Post from Joao",
    "title": "Mongo is fun",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime(2023, 11, 10, 10, 45),
    }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)
print("\nRecuperação FInal")
pprint.pprint(db.posts.find_one({"author": "Joao"}))

print("\nDocumentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)