import pymongo
client = pymongo.MongoClient("mongodb+srv://Dishant19:Dishant19@cluster0.lwbln6v.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)

d={
    'name':'Dishant',
    'surname':'Salunke'
}

d={
    'name':'Dishant',
    'ph no':8698
    'surname':'Salunke'
}

db1= client['mongotest']
coll =db1['test']
coll.insert_one(d)