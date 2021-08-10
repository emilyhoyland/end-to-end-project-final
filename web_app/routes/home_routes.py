
#importing libraries and files
from flask import Blueprint, request, render_template
from app.stock_sentiment import lookup_ticker
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")

def index(): #calling the home HTM template
    print("HOME...")
    #return "Welcome Home to the ticker sentiment app"
    return render_template("home.htm")


@home_routes.route("/about")
def about(): #calling the about HTML template
    print("About...")
    #return "About Me - I can tell you the sentiment for past few days"
    return render_template("about.htm")

@home_routes.route("/hello")
def hello_world(): #Calling the hello HTM template
    print("Welcome....", dict(request.args))
    name = request.args.get("name") or "Investor"
    message = f"Hello {name}!"
    # return message
    return render_template('hello.htm', message=message)

