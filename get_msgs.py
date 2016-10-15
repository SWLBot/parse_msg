# encoding=utf-8
from connect_mongo import connect_mongo
from jieba import jieba

client = connect_mongo()
db = client['nctu_development']

msgs = db['messages'].find()
strings=[]
for msg in msgs:
    sub = msg['content'].split()
    print(msg['content'])
    print(sub)
    strings = strings + sub
#print(strings)
segs = []
for str in strings:
    seglist = jieba.lcut(str,cut_all=False)
    print("Deault Mode: "+"/ ".join(seglist))
    segs = segs + seglist

with open("seg.dat","w") as f:
    for seg in segs:
        f.write(seg)
        f.write("\n")
client.close()
