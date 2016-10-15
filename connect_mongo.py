# encoding=utf-8
from pymongo import MongoClient
def connect_mongo():

    client = MongoClient("localhost")
    return client

