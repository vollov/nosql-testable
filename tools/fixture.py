
import settings as app_settings
import os, json, ast

from nosql.mongo import DBManager

from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class Fixture():

    def __init__(self):
        base_dir = app_settings.BASE_DIR
        self.data_dir = os.path.join(base_dir,'tests','data')
        
        
    def load(self, collection_name):
        '''
        Load collection from a json file
        1) parse file_name without json extension
        2) parse file as json objects 
        3) load json file into db
        '''
        
        docs = self._load_json_file(collection_name)
        print 'import collection = {0}'.format(collection_name)
        db_handler = DBManager.get_connection()
        db_handler[collection_name].insert_many(docs)
        
#     def _parse_file_name(self, file_base_name):
#         '''
#         get collection name: e.g. parse user.json to user
#         '''
#         return os.path.splitext(file_base_name)[0]
        
    def _load_json_file(self, collection_name):
        '''load a json file into memeory
        
        e.g. return data[0]["id"]
        '''
        json_file_name = collection_name + '.json'
        json_file_path = os.path.join(self.data_dir, json_file_name)
        
        with open(json_file_path) as file_handler:    
            data = json.load(file_handler)
        
        collection = []
        for item in data:
            collection.append(self._load_object_id(item))
        return collection
    
    def _load_object_id(self, item):
        item = ast.literal_eval(item)
        
        # if item has '_id' convert _id string to ObjectId
        if item['_id']:
            item['_id'] = ObjectId(item['_id'])
            
        return item

    def _encrypt_password(self, item):
        pass

    def dump(self, collection_name):
        '''
        write collection into a json file
        
        1) read collections
        2) write collections into json file
        '''

        print 'export collection = {0}'.format(collection_name)
        
        json_file_name = collection_name + '.json'
        json_file_path = os.path.join(self.data_dir, json_file_name)

        db_handler = DBManager.get_connection()
        iterator = db_handler[collection_name].find()
        collection = []
        for item in iterator:
            item = JSONEncoder().encode(item)
            collection.append(item)
        
        with open(json_file_path, 'w') as file_handler:
            json.dump(collection, file_handler)
        
