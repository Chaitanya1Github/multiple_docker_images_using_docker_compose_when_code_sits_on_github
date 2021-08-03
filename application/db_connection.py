import pymongo


# to connect with docker container
def get_db():
    MONGODB_HOST = "db"
    MONGODB_PORT = 27017

    client = pymongo.MongoClient(host=MONGODB_HOST,
                                 port=MONGODB_PORT,
                                 username='root',
                                 password='pass',
                                 authSource="admin")
    db = client["emp_db"]
    return db


# to connect locally to test on local machine first
# def get_db():
#     MONGODB_HOST = "localhost"
#     MONGODB_PORT = 27017
#
#     client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT,)
#     db = client["emp_db"]
#     return db
