from flask import *
from gevent.pywsgi import WSGIServer
from waitress import serve

app = Flask(__name__)


@app.route("/image/<name>", methods=["GET"])
def img_route(name):
    if request.args.get("api", default="", type=str) == "hieu987":
        src_img = f"images/{name}"
        return send_file(
            src_img,
            mimetype="image/gif",
        )


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=7777)
    serve(app, host="0.0.0.0", port=7777)
    # http_server = WSGIServer(("", 5000), app)
    # http_server.serve_forever()
