def route(app):
    # Movie slug
    from routes.MovieRoutes import movie_slug

    @app.route("/movie/<slug>", methods=["GET"])
    def movie_routes(slug):
        return movie_slug(slug)

    # Tv slug
    from routes.TvRoutes import tv_slug

    @app.route("/tv/<slug>", methods=["GET"])
    def tv_routes(slug):
        return tv_slug(slug)

    # Image
    from routes.ImageRoutes import get_image

    @app.route("/image/<name>", methods=["GET"])
    def image_routes(name):
        return get_image(name)

    # Detail movie, tv
    from routes.DetailRoutes import detail_movie_tv

    @app.route("/<type>/detail/<id>", methods=["GET"])
    def detail_routes(type, id):
        return detail_movie_tv(type, id)

    # Tv seasons
    from routes.TvSeasonsRoutes import tv_seasons

    @app.route("/tv/<id>/season/<season_number>", methods=["GET"])
    def tv_seasons_routes(id, season_number):
        return tv_seasons(id, season_number)

    # Rating
    from routes.RatingRoutes import rating_movie_tv

    @app.route("/<type>/rating/<id>", methods=["POST"])
    def rating_routes(type, id):
        return rating_movie_tv(type, id)

    # Trending
    from routes.TrendingRoutes import trending

    @app.route("/trending/<type>", methods=["GET"])
    def trending_routes(type):
        return trending(type)

    # Search
    from routes.SearchRoutes import search

    @app.route("/search/<type>", methods=["GET"])
    def search_routes(type):
        return search(type)

    # Get genres
    from routes.GenresRoutes import genres

    @app.route("/genre/<type>", methods=["GET"])
    def genres_routes(type):
        return genres(type)

    # Get years
    from routes.YearsRoutes import years

    @app.route("/year/<type>", methods=["GET"])
    def years_routes(type):
        return years(type)

    # Get countries
    from routes.CountriesRoutes import countries

    @app.route("/country/<type>", methods=["GET"])
    def countries_routes(type):
        return countries(type)

    # Discover
    from routes.DiscoverRoutes import discover

    @app.route("/discover/<type>", methods=["GET"])
    def discover_routes(type):
        return discover(type)

    # Authentication

    ## Login Facebook
    from routes.AuthenticateRoutes import loginfacebook

    @app.route("/auth/loginfacebook", methods=["POST"])
    def loginfacebook_routes():
        return loginfacebook()

    ## Log in
    from routes.AuthenticateRoutes import login

    @app.route("/auth/login", methods=["POST"])
    def login_routes():
        return login()

    ## Sigin up
    from routes.AuthenticateRoutes import signup

    @app.route("/auth/signup", methods=["POST"])
    def signup_routes():
        return signup()

    ## Get user by token
    from routes.AuthenticateRoutes import getuser_by_token

    @app.route("/auth/getusertoken", methods=["POST"])
    def getuser_by_token_routes():
        return getuser_by_token()

    # List

    ## Get list
    from routes.ListRoutes import getlist

    @app.route("/list/<idlist>/getlist", methods=["GET"])
    def getlist_routes(idlist):
        return getlist(idlist)

    ## Add item to list
    from routes.ListRoutes import additem_list

    @app.route("/list/<idlist>/add_item", methods=["POST"])
    def additem_list_routes(idlist):
        return additem_list(idlist)

    ## Remove item to list
    from routes.ListRoutes import removetem_list

    @app.route("/list/<idlist>/remove_item", methods=["POST"])
    def removeitem_list_routes(idlist):
        return removetem_list(idlist)
