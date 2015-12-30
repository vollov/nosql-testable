
import settings as app_settings
import os, json

from nosql.mongo import DBManager

class Fixture():

    def __init__(self):
        base_dir = app_settings.BASE_DIR
        self.data_dir = os.path.join(base_dir,'tests','data')
        
        
    def load(self, json_file_name):
        '''
        Load collection from a json file
        1) parse file_name without json extension
        2) parse file as json objects 
        3) load json file into db
        '''
        collection_name = self._parse_file_name(json_file_name)
        docs = self._load_json_file(json_file_name)
        db_handler = DBManager.get_connection()
        db_handler[collection_name].insert(docs, safe=True)
        
    def _parse_file_name(self, file_base_name):
        '''
        get collection name: e.g. parse user.json to user
        '''
        return os.path.splitext(file_base_name)[0]
        
    def _load_json_file(self, json_file_name):
        '''load a json file into memeory
        
        e.g. return data[0]["id"]
        '''
        json_file_path = os.path.join(self.data_dir, json_file_name)
        
        with open(json_file_path) as file_handler:    
            data = json.load(file_handler)
        
        return data
    
    def dump(self, collection_name):
        '''
        write collection into a json file
        
        1) read collections
        2) write collections into json file
        '''
        pass
        
