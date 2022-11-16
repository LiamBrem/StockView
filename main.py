from flask import Flask, request, render_template
import api_functions

app = Flask(__name__)


def fetchStockInfo(symbol):
    return str(api_functions.stockInfo(symbol))

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol", "")

        return render_template("displayStock.html", info=fetchStockInfo(symbol))

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
