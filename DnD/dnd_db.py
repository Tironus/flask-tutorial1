from bson.objectid import ObjectId

def create_doc(mongo_db, name, attr1=None, attr2=None, attr3=None):
    character = {
        'name' : name,
        'strength' : attr1,
        'dexterity' : attr2,
        'attr3' : attr3,
    }

    result = mongo_db.dnd.insert_one(character)
    return result

def display_name(mongo_db, name):
    result_list = []
    result = mongo_db.dnd.find({'name' : name})
    for doc in result:
        result_list.append(doc)
    return result_list

def display_id(mongo_db, id):
    result = mongo_db.dnd.find({'_id' : ObjectId(id)})
    for doc in result:
        return doc