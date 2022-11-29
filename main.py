from flask import Flask, request, render_template, redirect, url_for
import api_functions

#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.figure import Figure
import base64
from io import BytesIO

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        if request.form.get("submit") == "recommended":
            print("\nrecommended")
            return redirect(url_for('reddit'))
            

        else: 
            symbol = request.form.get("symbol", "")
            period = request.form.get("submit")
            interval = selectInterval(period)

            # Save it to a temporary buffer.
            fig = api_functions.retrieveGraph(symbol, period, interval)
            buf = BytesIO()
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            ###

            return render_template("displayStock.html", info=symbol, image=f"data:image/png;base64,{data}")

    return render_template("index.html")

@app.route("/reddit")
def reddit():
    return render_template('redditSuggestions.html')


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
