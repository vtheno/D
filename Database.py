#coding=utf-8
from json import loads,dumps
class FieldObject(object):
    __doc__ = """
    exist: Collection, the mean is the collection element have this field 
    not_exist: Collection, the mean is the collection element not have this field 
    __eq__(self, obj: object): Collection, the meaning is the collection element field equal obj
    __gt__(self, obj: object): Collection, like __eq__
    __ge__(self, obj: object): Collection, like __eq__
    __lt__(self, obj: object): Collection, like __eq__
    __le__(self, obj: object): Collection, like __eq__
    __ne__(self, obj: object): Collection, like __eq__
    """
    def __init__(self,field_name, collection: "Collection"):
        self.collection = collection
        self.field_name = field_name
    def update(self, value):
        f"""
        precondition is list element dict object have a only id
        update all key euqal {self.field_name}, value from argument
        """
        for item in self.collection.tables:
            item[self.field_name] = value
    @property
    def exist(self):
        return Collection([item for item in self.collection.tables if not item.get(self.field_name,None) is None])
    @property
    def not_exist(self):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) is None])
    def __eq__(self, obj):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) == obj])
    def __gt__(self, obj):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) > obj])
    def __ge__(self, obj):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) >= obj])
    def __lt__(self, obj):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) < obj])
    def __le__(self, obj):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) <= obj])
    def __ne__(self):
        return Collection([item for item in self.collection.tables if item.get(self.field_name,None) != obj])
class Field(object):
    __doc__ = """
    if obj = Field(collection)
    then obj.name, mean is name is a collection field 
    """
    def __init__(self, collection: "Collection"):
        for key in collection.keys:
            setattr(self,key,FieldObject(key, collection))
class Collection(object):
    def __init__(self,tables=[],keys=[]):
        self.tables = tables
        self.keys = keys
        if self.tables and self.keys == []:
            self.update_keys()
    def update_keys(self):
        """
        buildin function, don't use it
        """
        for i in self.tables:
            self.keys += [z for z in i.keys() if z not in self.keys]
    def insert(self, Map: "{str: [int | str | bool]}"):
        """
        insert(Map: dict)
        important !!!
        don't use (collection.field.field_name == xxxx).insert(Map) and anything 
        because field.field_name is a FieldObject, it will return a new collection,
        but we database using a collection it have a id, you can see different id.
        remove like this!!
        """
        self.keys += [z for z in Map.keys() if z not in self.keys]
        self.tables.append(Map)
    def remove(self, Map: "{str: [int | str | bool]}"):
        """
        remove(Map: dict)
        if Map in collection
        then remove it
        """
        if Map in self.tables:
            self.tables.remove(Map)
    @property
    def field(self):
        """
        field is a Field instance
        """
        return Field(self)
    def __repr__(self):
        return f"< Collection of {id(self)} >"
    def __iter__(self):
        return (i for i in self.tables)

class Database(object):
    def __init__(self, filename):
        self.filename = filename
    def open(self):
        with open(self.filename, 'r', encoding='utf-8') as fp:
            data = str(fp.read())
            json = loads(data,encoding='utf-8')
        self.data = Collection(json)
        return self.data
    def write(self):
        with open(self.filename, 'w', encoding='utf-8') as fp:
            data = dumps(self.data.tables)
            fp.write( data )
    def __repr__(self):
        return f"< Database of {id(self)} >"

__all__ = ["FieldObject","Field","Collection","Database"]

