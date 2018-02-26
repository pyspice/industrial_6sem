from pymongo import MongoClient

db = MongoClient(host='db', )['docker']

for line in db['msgs'].find():
    print(line)   
print('done')
