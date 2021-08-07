

from flask import Blueprint, request, jsonify, render_template

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
    