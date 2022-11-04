from flask import Flask, request, render_template

app = Flask(__name__)

def multiplyByThree(number):
    try:
        return str(int(number) * 3)
    except ValueError:
        return "Not a number"


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol", "")
    
        return "Your symbol is " + symbol

    return render_template("index.html")    

    #"""<form action="" method="get">
    #            Initial Number: <input type="text" name="number">
    #            <input type="submit" value="Multiply by 3">
    #        </form>"""
    #    + "final Num: "
    #    + finalNumber


if __name__ == '__main__':
   app.run(debug = True)