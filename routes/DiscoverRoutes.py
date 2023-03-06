import pymongo
from pymongo.errors import PyMongoError
from untils.JsonResponse import ConvertJsonResponse as cvtJson
from untils.ErrorMessage import errorMessage
from untils.Discover import discover_movie
from untils.Discover import discover_tv
from flask import *

myclient = pymongo.MongoClient(
    "mongodb+srv://admin:hieusen123@the-movie-database.fczrzon.mongodb.net/Phimhay247_DB"
)

db = myclient["Phimhay247_DB"]


def discover(type):
    try:
        page = request.args.get("page", default=1, type=int) - 1

        sort_by = request.args.get("sort_by", default="", type=str)
        primary_release_date_gte = request.args.get(
            "primary_release_date_gte", default="", type=str
        )
        primary_release_date_lte = request.args.get(
            "primary_release_date_lte", default="", type=str
        )

        with_genres = request.args.get("with_genres", default="", type=str)

        with_original_language = request.args.get(
            "with_original_language", default="", type=str
        )

        def convert_release_date(date_gte, data_lte):
            if date_gte != "":
                return {
                    "release_date": {
                        "$gte": date_gte,
                        "$lt": data_lte,
                    }
                }

            elif date_gte == "" and data_lte != "":
                return {
                    "release_date": {
                        "$lt": data_lte,
                    }
                }
            return {}

        def convert_first_air_date(date_gte, data_lte):
            if date_gte != "":
                return {
                    "first_air_date": {
                        "$gte": date_gte,
                        "$lt": data_lte,
                    }
                }

            elif date_gte == "" and data_lte != "":
                return {
                    "first_air_date": {
                        "$lt": data_lte,
                    }
                }

            return {}

        release_date = convert_release_date(
            primary_release_date_gte, primary_release_date_lte
        )

        first_air_date = convert_first_air_date(
            primary_release_date_gte, primary_release_date_lte
        )

        def conver_genres(genre):
            if genre != "":
                return {
                    "genres": {
                        "$elemMatch": {
                            # "id": int(with_genres.split(",")[0]),
                            # "name": with_genres.split(",")[1],
                            "id": int(with_genres)
                        }
                    }
                }
            else:
                return {}

        genres = conver_genres(with_genres)

        def convert_original_language(language):
            if language != "":
                return {"original_language": {"$regex": with_original_language}}
            else:
                return {}

        original_language = convert_original_language(with_original_language)

        if type == "all":
            if sort_by != "":
                if sort_by == "popularity_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("popularity", pymongo.DESCENDING)],
                        10,
                    )
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("popularity", pymongo.DESCENDING)],
                        10,
                    )
                    return {"results": movie + tv}
                elif sort_by == "release_date_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("release_date", pymongo.DESCENDING)],
                        10,
                    )
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("first_air_date", pymongo.DESCENDING)],
                        10,
                    )
                    return {"results": movie + tv}
                elif sort_by == "revenue_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("revenue", pymongo.DESCENDING)],
                        10,
                    )
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("revenue", pymongo.DESCENDING)],
                        10,
                    )
                    return {"results": movie + tv}
                elif sort_by == "vote_average_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [
                            ("vote_count", pymongo.DESCENDING),
                            ("vote_average", pymongo.DESCENDING),
                        ],
                        10,
                    )
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [
                            ("vote_count", pymongo.DESCENDING),
                            ("vote_average", pymongo.DESCENDING),
                        ],
                        10,
                    )
                    return {"results": movie + tv}
            else:
                movie = discover_movie(
                    release_date,
                    genres,
                    original_language,
                    page,
                    None,
                    10,
                )
                tv = discover_tv(
                    first_air_date,
                    genres,
                    original_language,
                    page,
                    None,
                    10,
                )
                return {
                    "results": movie + tv,
                }

        elif type == "movieall":
            if sort_by != "":
                if sort_by == "popularity_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("popularity", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": movie}
                elif sort_by == "release_date_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("release_date", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": movie}
                elif sort_by == "revenue_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [("revenue", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": movie}
                elif sort_by == "vote_average_desc":
                    movie = discover_movie(
                        release_date,
                        genres,
                        original_language,
                        page,
                        [
                            ("vote_count", pymongo.DESCENDING),
                            ("vote_average", pymongo.DESCENDING),
                        ],
                        20,
                    )

                    return {"results": movie}
            else:
                movie = discover_movie(
                    release_date,
                    genres,
                    original_language,
                    page,
                    None,
                    20,
                )

                return {
                    "results": movie,
                }

        elif type == "tvall":
            if sort_by != "":
                if sort_by == "popularity_desc":
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("popularity", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": tv}
                elif sort_by == "release_date_desc":
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("release_date", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": tv}
                elif sort_by == "revenue_desc":
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [("revenue", pymongo.DESCENDING)],
                        20,
                    )

                    return {"results": tv}
                elif sort_by == "vote_average_desc":
                    tv = discover_tv(
                        first_air_date,
                        genres,
                        original_language,
                        page,
                        [
                            ("vote_count", pymongo.DESCENDING),
                            ("vote_average", pymongo.DESCENDING),
                        ],
                        20,
                    )

                    return {"results": tv}
            else:
                tv = discover_tv(
                    first_air_date,
                    genres,
                    original_language,
                    page,
                    None,
                    20,
                )

                return {
                    "results": tv,
                }

        else:
            return errorMessage(400)

    except:
        return {"results": []}
