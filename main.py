from flask import *
from waitress import serve
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/image/<name>", methods=["GET"])
def img_route(name):
    src_img = f"./images/{name}"
    return send_file(
        src_img,
        mimetype="image/gif",
    )


if __name__ == "__main__":
    # app.run(debug=True, port=5000, use_reloader=True)
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
