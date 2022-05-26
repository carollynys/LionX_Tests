"""
Have you heard about singleton?
Have you used any python library that connects with a database?
If you did it, try to implement a singleton usage of it.
"""

import pymongo


class MongoSingletonConecction:
    __instance = None

    @staticmethod
    def get_instance():
        if MongoSingletonConecction.__instance == None:
            MongoSingletonConecction()

        return MongoSingletonConecction.__instance

    def __init__(self):
        if MongoSingletonConecction.__instance != None:
            raise Exception("It's a singleton!!!")
        else:
            MongoSingletonConecction.__instance = pymongo.MongoClient(
                'localhost', 27017).connect


connection = MongoSingletonConecction()
print(connection.get_instance())
