from flask import Flask, request, render_template
import api_functions

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        symbol = request.form.get("symbol", "")

        period = request.form.get("submit")

        interval = selectInterval(period)

        #Figure out how to put this into a seperate function
        

        return render_template("displayStock.html", info=fetchStockInfo(symbol, period, interval))

    return render_template("index.html")


def fetchStockInfo(symbol, period, interval):
    return str(api_functions.stockInfo(symbol, period, interval))

def selectInterval(period):
    if period == "1d":
        interval = "1m"
    elif period == "1wk":
        interval = "1h"
    elif period == "1mo":
        interval = "1d"
    elif period == "6mo":
        interval = "1d"
    elif period == "1y":
        interval = "1wk"

    return interval



if __name__ == '__main__':
    app.run(debug=True)
