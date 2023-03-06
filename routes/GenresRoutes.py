import pymongo
from pymongo.errors import PyMongoError
from untils.JsonResponse import ConvertJsonResponse as cvtJson
from untils.ErrorMessage import errorMessage
from flask import *

myclient = pymongo.MongoClient(
    "mongodb+srv://admin:hieusen123@the-movie-database.fczrzon.mongodb.net/Phimhay247_DB"
)

db = myclient["Phimhay247_DB"]


def genres(type):
    try:
        if type == "all":
            genres = cvtJson(db["genres"].find())
            return genres
        else:
            return errorMessage(400)
    except:
        return []
