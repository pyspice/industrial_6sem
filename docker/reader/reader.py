from pymongo import MongoClient

db = MongoClient(host='db', port=27017)['docker']

for line in db['msgs'].find():
    print(line)   
print('done')
