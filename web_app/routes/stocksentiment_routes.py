

from flask import Blueprint, request, jsonify, render_template, redirect

from app.stock_sentiment import lookup_ticker

stocksentiment_routes = Blueprint("stocksentiment_routes", __name__)

@stocksentiment_routes.route("/stock/sentiment.json")
def stock_sentiment_api():
    print("STOCK SENTIMENT (API)...")
    print("URL PARAMS:", dict(request.args))

    stock_name = request.args.get("stock_name") or "AMAZON"
    ticker=request.args.get("ticker") or "amzn"

    results = lookup_ticker(ticker)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid ticker or stock name. Please try again"}), 404


@stocksentiment_routes.route("/stock/form")
def stock_form():
    print("STOCK FORM...")
    return render_template("stockticker_form.htm")


@stocksentiment_routes.route("/stock/sentiment", methods=["GET", "POST"])
def stocksentiment_score():
    print("STOCK SENTIMENT SCORE...")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    ticker = request_data.get("ticker") or "AMZN"
    #zip_code = request_data.get("zip_code") or "20057"

    results = lookup_ticker(ticker=ticker)
    if results:
        #flash("Weather Forecast Generated Successfully!", "success")
        return render_template("stock_sentiment.htm", ticker=ticker, results=results)
    else:
        #flash("Geography Error. Please try again!", "danger")
        return redirect("/stock/form")
