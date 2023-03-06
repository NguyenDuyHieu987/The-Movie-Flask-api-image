from flask import *


def get_image(name):
    print(name)
    src_img = f"images/{name}"
    return send_file(
        src_img,
        mimetype="image/gif",
    )
