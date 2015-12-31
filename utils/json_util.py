import json, ast
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

class JsonUtil:
    '''
    json.dumps(obj) -- Serialize obj to a JSON formatted str
    json.loads(str) -- Unserialize a JSON object from a string s 
    '''

    @staticmethod
    def itemToStr(item):
        '''
        for item returned from mongodb query
        filter out unicode, and convert ObjectId(_id) to str(_id)
        '''
        item = JSONEncoder().encode(item)
        return ast.literal_eval(item)

    @staticmethod
    def listToStr(items):
        '''
        convert ObjectId(_id) to str(_id) for each item 
        '''
        collection = []
        for item in items:
            collection.append(JsonUtil.itemToStr(item))
        return collection
