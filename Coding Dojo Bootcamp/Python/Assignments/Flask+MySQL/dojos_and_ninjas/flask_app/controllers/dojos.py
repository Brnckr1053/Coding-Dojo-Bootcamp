from flask_app import app
from flask import render_template
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")
