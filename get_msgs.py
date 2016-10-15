# encoding=utf-8
from connect_mongo import connect_mongo

client = connect_mongo()
db = client['nctu_development']

msgs = db['messages'].find()

for msg in msgs:
    print(msg['content'])
    print("//////////////")


client.close()
