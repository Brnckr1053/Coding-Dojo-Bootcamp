from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",dojos = dojos)


@app.route("/create/dojo", methods =['POST'])
def create_dojo():
    Dojo.insert_dojos(request.form)
    return redirect("/dojos")


@app.route("/dojo/<int:id>")
def dojo_inside(id):
    data = {
        "id":id
    }
    return render_template("dojo.html", dojo = Dojo.show_ninja(data))