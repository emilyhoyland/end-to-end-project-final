

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
@home_routes.route("/home")

def index():
    print("HOME...")
    return "Welcome Home"

@home_routes.route("/about")
def about():
    print("About...")
    return "About Me"