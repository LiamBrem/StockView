from flask import Flask, request, render_template
import requests

API_KEY = "dQ_0vBbHkOiJyjlF4QQ8vK_Mq5Ss2eKp"

API_URL = (
    )
print(API_URL)

app = Flask(__name__)


def fetchStockInfo(symbol):
    API_URL = (f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey={API_KEY}")
    print(API_URL)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol", "")


        fetchStockInfo(symbol)
        return "Your symbol is " + symbol

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
