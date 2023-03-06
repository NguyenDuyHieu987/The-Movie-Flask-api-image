import pymongo
from pymongo.errors import PyMongoError
from untils.JsonResponse import ConvertJsonResponse as cvtJson
from untils.ErrorMessage import errorMessage
from flask import *
from pymongo import ReturnDocument

myclient = pymongo.MongoClient(
    "mongodb+srv://admin:hieusen123@the-movie-database.fczrzon.mongodb.net/Phimhay247_DB"
)

db = myclient["Phimhay247_DB"]


def getlist(idlist):
    list = db["lists"].find_one({"id": idlist})
    return cvtJson(list)


def additem_list(idlist):
    try:
        media_type = request.form["media_type"]
        media_id = request.form["media_id"]

        if media_type == "movie":
            movie = db["movies"].find_one(
                {"id": int(media_id)},
                {
                    "images": 0,
                    "credits": 0,
                    "videos": 0,
                    "production_companies": 0,
                },
            )

            if movie != None:
                db["lists"].find_one_and_update(
                    {"id": idlist},
                    {"$addToSet": {"items": movie}},
                    {"new": True},
                    return_document=ReturnDocument.AFTER,
                )
                return {"success": True, "results": "Add item to list suucessfully"}
            else:
                return {
                    "success": False,
                    "results": "Failed to add item to list",
                }

        elif media_type == "tv":
            tv = db["tvs"].find_one(
                {"id": int(media_id)},
                {
                    "images": 0,
                    "credits": 0,
                    "videos": 0,
                    "production_companies": 0,
                    "seasons": 0,
                },
            )
            if tv != None:
                db["lists"].find_one_and_update(
                    {"id": idlist},
                    {"$addToSet": {"items": tv}},
                    {"new": True},
                    return_document=ReturnDocument.AFTER,
                )
                return {"success": True, "results": "Add item to list suucessfully"}
            else:
                return {
                    "success": False,
                    "results": "Failed to add item to list",
                }
    except PyMongoError as e:
        return {"success": e._message}


def removetem_list(idlist):
    try:
        media_id = request.form["media_id"]

        db["lists"].find_one_and_update(
            {"id": idlist},
            {"$pull": {"items": {"id": int(media_id)}}},
            {"new": True},
            return_document=ReturnDocument.AFTER,
        )

        list = cvtJson(db["lists"].find_one({"id": idlist}))

        return {"success": True, "results": list["items"]}
    except PyMongoError as e:
        return {"success": False, "result": "Failed to remove item from list"}
