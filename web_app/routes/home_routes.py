

from flask import Blueprint, request, render_template, jsonify
from app.stock_sentiment import lookup_ticker
home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
@home_routes.route("/home")

def index():
    print("HOME...")
    #return "Welcome Home to the ticker sentiment app"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("About...")
    #return "About Me - I can tell you the sentiment for past few days"
    return render_template("about.html")
