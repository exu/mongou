
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
scores = db.grades


def find():

    query = {'type':'homework'}
    projection = {'student_id':1}

    try:
        cursor = scores.find(query)
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),
                              ('score',pymongo.ASCENDING)])

        print cursor

    except Exception as e:
        print "Unexpected error:", type(e), e

    last_id = None

    for doc in cursor:
        if  last_id != doc['student_id']:
            scores.remove({'_id': doc['_id']})

        last_id =  doc['student_id']

        print doc



find()
