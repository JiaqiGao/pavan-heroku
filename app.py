import os
import random
from flask import Flask, render_template, session, redirect, url_for

from func_utils import apifunctions


app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    address = request.form["address"]
    response = apifunctions.googlemap(address)
    
    return render_template("index.html", locate = response["location"])


if __name__ == "__main__":
    #config.load_keys()
    app.debug = True
    app.run()
