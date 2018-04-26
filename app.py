import os
import random
import config
import json
from flask import Flask, render_template, request, session, redirect, url_for

import apifunctions


app = Flask(__name__)

#@app.route("/")
@app.route("/", methods=["GET","POST"])
def index():
    config.load_keys()
    GOOGLE_MAP = config.keys["GOOGLE_MAPS_Javascript"]
    #return render_template("index.html")
    if request.method == "POST":
        address = request.form['address']
        response = apifunctions.googlemap(address)
        if response:
            location = response["location"]
            airquality = response["measurement"]
            return render_template("index.html", success=True, GOOGLE_MAP=GOOGLE_MAP, current_lat = json.dumps(response["coordinates"]["lat"]), current_lng = json.dumps(response["coordinates"]["lng"]), locate = location, airquality = airquality)
        return render_template("index.html", success=False, GOOGLE_MAP=GOOGLE_MAP)
    return render_template("index.html", success=False, GOOGLE_MAP=GOOGLE_MAP)


if __name__ == "__main__":
    config.load_keys()
    app.run()
