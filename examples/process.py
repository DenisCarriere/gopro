from pymongo import MongoClient


client = MongoClient()

for item in client.gopro.photos.find({},{'_id':0}):
    query = {'dt':
        {'$gt': item['dt']}
    }
    search = client.gopro.gpx.find_one(query, {'_id':0})
    item.update(search)
    client.gopro.process.save(item)