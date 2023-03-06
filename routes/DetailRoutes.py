import pymongo
from pymongo.errors import PyMongoError
from untils.JsonResponse import ConvertJsonResponse as cvtJson
from untils.ErrorMessage import errorMessage
from flask import *

myclient = pymongo.MongoClient(
    "mongodb+srv://admin:hieusen123@the-movie-database.fczrzon.mongodb.net/Phimhay247_DB"
)

db = myclient["Phimhay247_DB"]


def detail_movie_tv(type, id):
    try:
        append_to_response = request.args.get(
            "append_to_response", default="", type=str
        )
        exceptValue = {"images": 0, "credits": 0, "videos": 0}

        if append_to_response != "":
            if "images" in append_to_response.split(","):
                exceptValue.pop("images")
            if "credits" in append_to_response.split(","):
                exceptValue.pop("credits")
            if "videos" in append_to_response.split(","):
                exceptValue.pop("videos")

        if type == "movie":
            movie = cvtJson(db["movies"].find_one({"id": int(id)}, exceptValue))
            if movie != None:
                return movie
            else:
                return {"not_found": True}

        elif type == "tv":
            tv = db["tvs"].find_one({"id": int(id)}, exceptValue)
            if tv != None:
                return cvtJson(tv)
            else:
                return {"not_found": True}
        else:
            return errorMessage(400)
    except:
        return {}
