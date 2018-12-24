#coding=utf-8
from Database import *
db = Database('test.json')
db.open()
for idx,item in enumerate( db.data ):
    print( idx, item )
(db.data.field.age == 26).field.age.update(-1)
for idx,item in enumerate( db.data ):
    print( idx, item )
print( (db.data.field.age == 26) )
print( list((db.data.field.firstname == "Vtheno").field.age == -1) )
print( list((db.data.field.lastname == "Arthur").field.age > 0) )
