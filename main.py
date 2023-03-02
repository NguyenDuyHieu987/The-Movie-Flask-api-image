from flask import *
from gevent.pywsgi import WSGIServer


app = Flask(__name__)


@app.route("/image/<name>", methods=["GET"])
def img_route(name):
    if request.args.get("api", default="", type=str) == "hieu987":
        src_img = f"images/{name}"
        return send_file(
            src_img,
            mimetype="image",
        )
    return {}


if __name__ == "__main__":
    # app.run(port=7777)
    http_server = WSGIServer(("", 5001), app)
    http_server.serve_forever()
