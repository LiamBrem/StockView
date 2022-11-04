from flask import Flask, request, render_template
import requests

API_KEY = "dQ_0vBbHkOiJyjlF4QQ8vK_Mq5Ss2eKp"

app = Flask(__name__)


def fetchStockInfo(symbol):
    API_URL = (f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2022-11-03/2022-11-04?adjusted=true&sort=asc&limit=120&apiKey={API_KEY}")
    res = requests.get(API_URL)

    print(str(res.json()))

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol", "")

        fetchStockInfo(symbol)
        return "Your symbol is " + symbol

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
