from flask import Flask, request, render_template
import api_functions

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol", "")
        print("\n" + symbol)

        
        inputPeriod = request.form.get("dateInput")

<<<<<<< HEAD
        interval = checkInterval(inputPeriod)

        return render_template("displayStock.html", info=fetchStockInfo(symbol, inputPeriod, interval))
=======
        #Figure out how to put this into a seperate function
        if request.form.get('hour') == "1h":
            period = "1h"
            interval = "1m"
        elif request.form.get("day") == "1d":
            period = "1d"
            interval = "1m"
        elif request.form.get("week") == "1wk":
            period = "1wk"
            interval = "1d"
        elif request.form.get("month") == "1mo":
            period = "1mo"
            interval = "1d"
        elif request.form.get("sixmonths") == "6mo":
            period = "6mo"
            interval = "1d"
        elif request.form.get("year") == "1y":
            period = "1y"
            interval = "1wk"
            
            
            
        return render_template("displayStock.html", info=fetchStockInfo(symbol, period, interval))
>>>>>>> temp-branch

    return render_template("index.html")


def fetchStockInfo(symbol, period, interval):
    return str(api_functions.stockInfo(symbol, period, interval))


def checkInterval(inputPeriod):
    # default period/interval
    period = "1d"
    interval = "1m"

    if inputPeriod == "1h":
        period = "1h"
        interval = "1m"
    elif inputPeriod == "1d":
        period = "1d"
        interval = "1m"
    elif inputPeriod == "1wk":
        period = "1wk"
        interval = "1d"
    elif inputPeriod == "1mo":
        period = "1mo"
        interval = "1d"
    elif inputPeriod == "6mo":
        period = "6mo"
        interval = "1d"
    elif inputPeriod == "1y":
        period = "1y"
        interval = "1wk"

    return interval


if __name__ == '__main__':
    app.run(debug=True)
